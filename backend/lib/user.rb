require "rpc/user_service_services_pb"
require "rpc/auth_services_pb"
require "logs"
require "env"
require "stock"

USER = UserService::UserService::Stub.new(
  "#{Env::USER_SERVICE}:50051",
  :this_channel_is_insecure
)

AUTH = AuthService::Auth::Stub.new(
  "#{Env::AUTH_SERVICE}:50051",
  :this_channel_is_insecure
)

class User
  def initialize(name, stocks)
    @name = name
    @stocks = []
  end

  attr_reader :name

  def buy(code)
    LOGGER.debug("Buying #{code}...")
    request = UserService::StockToUserRequest.new(
      user: @name,
      stock_code: code
    )
    response = USER.add_stock_to_user(request)
    response.ok_code
  end

  def sell(code)
    LOGGER.debug("Selling #{code}...")
    request = UserService::StockToUserRequest.new(
      user: @name,
      stock_code: code
    )
    response = USER.remove_stock_from_user(request)
    response.ok_code
  end

  def self.login(name, password)
    LOGGER.debug("Logging user in...")
    request = AuthService::UserPasswordRequest.new(user: name, password: password)
    response = AUTH.get_token(request)
    token = response.token
    stocks = self.stocks(name)

    [User.new(name, stocks), token]
  end

  def self.authenticate(token)
    LOGGER.debug("Authenticating user...")
    request = AuthService::CheckTokenRequest.new(token: token)
    begin
      response = AUTH.check_token(request)
      LOGGER.debug("User successfully authenticated...")
      name = response.user
      stocks = self.stocks(name)
      User.new(name, stocks)
    rescue GRPC::InvalidArgument
      raise BadTokenError.new
    end
  end

  def self.signup(name, password)
    request = AuthService::UserPasswordRequest.new(
      user: name,
      password: password
    )
    response = AUTH.register_user(request)
    [User.new(name, []), response.token]
  end

  def to_json(*options)
    {name: @name, stocks: @stocks}.to_json(*options)
  end

  def self.stocks(name)
    LOGGER.debug("Getting user stocks...")
    request = UserService::GetUserStocksRequest.new(user: name)
    response = USER.get_stocks(request)
    response.codes.map { |code| Stock.new(code, "", 0) }
  end

  private_class_method :stocks
end

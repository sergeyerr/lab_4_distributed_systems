require "rpc/user_service_services_pb"
require "rpc/auth_services_pb"
require "env"
require "stock"

USER = UserService::UserService::Stub.new(
  "#{Env::USER}:50001",
  :this_channel_is_insecure
)

AUTH = AuthService::Auth::Stub.new(
  "#{Env::AUTH}:50000",
  :this_channel_is_insecure
)

class User
  def initialize(name, stocks, token)
    @name = name
    @stocks = []
  end

  def buy(code)
    request = UserService::StockToUserRequest(user: @name, stock_code: code)
    response = USER.add_stock_to_user(request)
    response.ok_code
  end

  def sell(code)
    request = UserService::StockToUserRequest(user: @name, stock_code: code)
    response = USER.remove_stock_from_user(request)
    response.ok_code
  end

  def self.login(name, password)
    request = AuthService::UserPasswordRequest.new(user: name, password: password)
    response = AUTH.get_token(request)
    token = response.token
    stocks = self.stocks(name)

<<<<<<< HEAD
    [User.new(name, stocks), token]
  end

  def self.authenticate(token)
    request = AuthService::CheckTokenRequest.new(token: token)
    response = AUTH.check_token(request)
    name = response.user
    if name != ""
      stocks = self.stocks(name)
      User.new(name, stocks)
    end
  end

  def self.signup(name, password)
=======
    User.new(name, stocks, token)
  end

  def self.authenticate(token)
    request = AuthService::CheckTokenRequest.new(token)
    response = AUTH.CheckToken(request)
    response.ok_code
  end

  def self.register(name, password)
>>>>>>> e0eb3809017b2d144d4165e794326a94e5baed6e
    request = AuthService::UserPasswordRequest.new(
      user: name,
      password: password
    )
    response = USER.register_user(request)
<<<<<<< HEAD
    [User.new(name, []), response.token]
=======
    User.new(name, stocks, response.token)
>>>>>>> e0eb3809017b2d144d4165e794326a94e5baed6e
  end

  def to_json(*options)
    {name: @name, stocks: @stocks, token: @token}.to_json(*options)
  end

<<<<<<< HEAD
  def self.stocks(name)
    request = UserService::GetUserStocksRequest.new(user: name)
    response = USER.get_stocks(request)
    response.codes.map { |code| Stock.new(code, "", 0) }
  end

  private_class_method :stocks
=======
  private

  def stocks(name)
    request = UserService::GetUserStocksRequest(user: name)
    response = USER.get_stocks(request)
    response.codes.map { |code| Stock.new(code, "", 0) }
  end
>>>>>>> e0eb3809017b2d144d4165e794326a94e5baed6e
end

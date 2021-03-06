import grpc
import Finance_API_pb2_grpc
import Finance_API_pb2
import time
import redis
from os import getenv
from redis.sentinel import Sentinel

update_frequency = getenv('UPDATE_FREQUENCY', '20')
finance_api_host = getenv('FINANCE_API', 'localhost')

redis_conn = redis.Redis()

if finance_api_host == 'localhost':
    redis_conn = redis.Redis()
else:
    sentinel = Sentinel([('redis-sentinel', '26379')], socket_timeout=0.1)
    redis_conn = sentinel.master_for('mymaster', socket_timeout=0.1, password='redis')


def update_stocks(stub):
    for stock in stub.get_stocks(Finance_API_pb2.Get_stocks_request()):
        redis_conn.hset('Stocks', stock.code, stock.name) 
        redis_conn.set(stock.code, stock.price[0])
        print(stock.name + " " + stock.code + " " + str(stock.price))


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel(finance_api_host + ':50051') as channel:
        stub = Finance_API_pb2_grpc.StocksLoaderStub(channel)

        while True:
            update_stocks(stub)
            time.sleep(int(update_frequency))


if __name__ == '__main__':
    run()

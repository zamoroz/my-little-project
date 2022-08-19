from concurrent import futures
import grpc

from pb import db_pb2_grpc
from servicers import (
    exchanges,
    orders,
    symbols,
    wallet
)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    db_pb2_grpc.add_ExchangesServicer_to_server(exchanges.Exchanges(), server)
    db_pb2_grpc.add_OrdersServicer_to_server(orders.Orders(), server)
    db_pb2_grpc.add_SymbolsServicer_to_server(symbols.Symbols(), server)
    db_pb2_grpc.add_WalletServicer_to_server(wallet.Wallet(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    print('DB server started')
    server.wait_for_termination()
    print('DB server terminated')

if __name__ == '__main__':
    serve()
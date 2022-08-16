from concurrent import futures
import grpc

from .pb import (
    orders_pb2_grpc,
    symbols_pb2_grpc,
    wallet_pb2_grpc
)
from .servicers import (
    orders,
    symbols,
    wallet
)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_pb2_grpc.add_OrdersServicer_to_server(orders.Orders(), server)
    symbols_pb2_grpc.add_SymbolsServicer_to_server(symbols.Symbols(), server)
    wallet_pb2_grpc.add_WalletServicer_to_server(wallet.Wallet(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
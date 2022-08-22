from os import getenv
from symtable import Symbol
import grpc

from pb import db_pb2_grpc
from pb import db_pb2

class Client():
    channel = grpc.insecure_channel(getenv('DB_API'))
    symbolsStub = db_pb2_grpc.SymbolsStub(channel)
    ordersStub = db_pb2_grpc.OrdersStub(channel)
    walletStub = db_pb2_grpc.WalletStub(channel)

    def get_symbols(self) -> list:
        response = self.symbolsStub.Read(db_pb2.ReadRequest(exchange='huobi'))
        symbols = []
        for i in response:
            symbols.append(i.symbol)
        return symbols

    def order_handler(self, data: dict):
        if data['eventType'] == 'deletion':
            self.ordersStub.Delete(db_pb2.DeleteOrder(
                exchange='huobi',
                symbol=data['symbol'],
                order_id=data['orderId']
                ))
        if data['eventType'] == 'creation':
            self.ordersStub.Create(db_pb2.OrderRequest(
                exchange='huobi',
                symbol=data['symbol'],
                order_id=data['orderId'],
                price=float(data['orderPrice']),
                qty=float(data['orderSize']),
                status='NEW',
                side=data['type'].split('-')[0].upper(),
                time=data['orderCreateTime']
            ))
        if data['eventType'] == 'trade':
            self.ordersStub.Update(db_pb2.OrderRequest(
                exchange='huobi',
                symbol=data['symbol'],
                order_id=data['orderId'],
                price=float(data['orderPrice']),
                qty=float(data['orderSize']),
                status='FILLED',
                side=data['type'].split('-')[0].upper(),
                time=data['orderCreateTime']
            ))

    def wallet_handler(self, data: dict):
        self.walletStub.Update(db_pb2.WalletRequest(
            exchange='huobi',
            coin=data['currency'],
            amount=data['available']
        ))

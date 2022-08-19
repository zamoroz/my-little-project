from pb import db_pb2
from pb import db_pb2_grpc
from db.db import Exchanges as exchanges_doc, Orders, Symbols, Wallet


class Exchanges(db_pb2_grpc.ExchangesServicer):

    def Create(self, request, context) -> db_pb2.CommonReply:
        for i in exchanges_doc.objects():
            if i.name == request.name:
                return db_pb2.CommonReply(code=500, message='Exchange already set')

        ex = exchanges_doc(request.name)
        # TODO Exchanges client
        '''
        ex.symbols = []
        for i in request.symbols:
            ex.symbols.append(symbols_client.get_symbol_doc(i))

        ex.orders = []
        for i in symbols:
            for j in orders_client.get_orders_doc(i):
                ex.orders.append(j)

        ex.wallet = get_wallet_doc()

        ex.save()'''
        return db_pb2.CommonReply(code=200, message='Exchange created')

    def Read(self, request, context):
        return super().Read(request, context)

    def Update(self, request, context):
        return super().Update(request, context)

    def Delete(self, request, context):
        return super().Delete(request, context)

def get_exchange_entity(exchange_name:str):
    for i in exchanges_doc.objects():
        if i.name == exchange_name:
            return(i)
    else: return None
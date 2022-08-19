from pb import db_pb2, db_pb2_grpc
from .exchanges import get_exchange_entity

class Wallet(db_pb2_grpc.WalletServicer):

    def Create(self, request, context):
        #TODO Exchange client
        return super().Create(request, context)

    def Read(self, request, context) -> db_pb2.WalletReply:
        response = db_pb2.WalletReply()
        exchange = get_exchange_entity(request.exchange)
        for i in exchange.wallet:
            response.request.append(db_pb2.WalletReply(
                exchange=request.exchange,
                coin=i.coin,
                amount=i.amount
            ))
        return response

    def Update(self, request, context) -> db_pb2.CommonReply:
        exchange = get_exchange_entity(request.exchange)
        if not exchange:
            return db_pb2.CommonReply(code=404, message='Exchange not found')
        for i in exchange.wallet:
            if request.coin == i.coin:
                i.amount = request.amount
                exchange.save()
                return db_pb2.CommonReply(code=200, message='Wallet updated')
        else: return db_pb2.CommonReply(code=404, message='Coin not found')
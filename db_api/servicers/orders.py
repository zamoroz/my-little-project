from pb import db_pb2
from pb import db_pb2_grpc
from db.db import Orders as order_doc
from .exchanges import get_exchange_entity

class Orders(db_pb2_grpc.OrdersServicer):

    def Create(self, request, context):
        #TODO Exchanges client
        return super().Create(request, context)

    def Add(self, request, context) -> db_pb2.CommonReply:
        order = order_doc(
            symbol=request.symbol,
            order_id=request.order_id,
            price=request.price,
            qty=request.qty,
            status=request.status,
            side=request.side,
            time=request.time
        )
        exchange = get_exchange_entity(request.exchange)
        if not exchange:
            return db_pb2.CommonReply(code=404, message='Exchange not found')
        exchange.orders.append(order)
        exchange.save()
        return db_pb2.CommonReply(code=200, message='Order created')

    def Read(self, request, context) -> db_pb2.OrdersReply:
        response = db_pb2.OrdersReply()
        exchange = get_exchange_entity(request.exchange)
        for i in exchange.orders:
            response.request.append(db_pb2.OrderRequest(
                exchange=request.exchange,
                symbol=i.symbol,
                order_id=i.order_id,
                price=i.price,
                qty=i.qty,
                status=i.status,
                side=i.side,
                time=i.time
            ))
        return response

    def Update(self, request, context) -> db_pb2.CommonReply:
        exchange = get_exchange_entity(request.exchange)
        if not exchange:
            return db_pb2.CommonReply(code=404, message='Exchange not found')
        for i in exchange.orders:
            if request.order_id == i.order_id:
                i.status = request.status
                exchange.save()
                return db_pb2.CommonReply(code=200, message='Order updated')
        else: return self.Create(request, context)

    def Delete(self, request, context) -> db_pb2.CommonReply:
        exchange = get_exchange_entity(request.exchange)
        if not exchange:
            return db_pb2.CommonReply(code=404, message='Exchange not found')
        for i in exchange.orders:
            if i.order_id == request.order_id:
                exchange.orders.remove(i)
                exchange.save()
                return db_pb2.CommonReply(code=200, message='Order removed')
        else: return db_pb2.CommonReply(code=404, message='Order not found')

    def Count(self, request, context) -> db_pb2.CountReply:
        exchange = get_exchange_entity(request.exchange)
        if not exchange:
            return db_pb2.CountReply(count=0)
        return db_pb2.CountReply(count=len(exchange.orders))
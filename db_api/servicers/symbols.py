from pb import db_pb2, db_pb2_grpc
from db.db import Symbols as symbol_doc
from .exchanges import get_exchange_entity


class Symbols(db_pb2_grpc.SymbolsServicer):

    def Create(self, request, context) -> db_pb2.CommonReply:
        exchange = get_exchange_entity(request.exchange)
        if not exchange:
            return db_pb2.CommonReply(code=404, message='Exchange not found')
        for i in exchange.symbols:
            if i.symbol == request.symbol:
                db_pb2.CommonReply(code=500, message='Symbol already set')
        else:
            exchange.symbols.append(symbol_doc(
                symbol=request.symbol,
                base_asset=request.base_asset,
                quote_asset=request.quote_asset,
                qty_rounder=request.qty_rounder,
                price_rounder=request.price_rounder
            ))
            exchange.save()
            return db_pb2.CommonReply(code=200, message='Symbol created')

    def Read(self, request, context) -> db_pb2.SymbolsReply:
        response = db_pb2.SymbolsReply()
        exchange = get_exchange_entity(request.exchange)
        for i in exchange.symbols:
            response.request.append(db_pb2.SymbolsReply(
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

    def Update(self, request, context)-> db_pb2.CommonReply:
        exchange = get_exchange_entity(request.exchange)
        if not exchange:
            return db_pb2.CommonReply(code=404, message='Exchange not found')
        for i in exchange.symbols:
            if request.order_id == i.order_id:
                i.status = request.status
                exchange.save()
                return db_pb2.CommonReply(code=200, message='Order updated')
        else: return self.Create(request, context)

    def Delete(self, request, context) -> db_pb2.CommonReply:
        exchange = get_exchange_entity(request.exchange)
        if not exchange:
            return db_pb2.CommonReply(code=404, message='Exchange not found')
        for i in exchange.symbols:
            if i.order_id == request.order_id:
                exchange.symbols.remove(i)
                exchange.save()
                return db_pb2.CommonReply(code=200, message='Order removed')
        else: return db_pb2.CommonReply(code=404, message='Order not found')

    def Count(self, request, context) -> db_pb2.CountReply:
        exchange = get_exchange_entity(request.exchange)
        if not exchange:
            return db_pb2.CountReply(count=0)
        return db_pb2.CountReply(count=len(exchange.symbols))
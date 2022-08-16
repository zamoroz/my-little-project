from ..pb import orders_pb2
from ..pb import orders_pb2_grpc

class Orders(orders_pb2_grpc.OrdersServicer):

    def Load(self, request, context):
        return super().Load(request, context)

    def Create(self, request, context):
        return super().Create(request, context)

    def Read(self, request, context):
        return super().Read(request, context)

    def Update(self, request, context):
        return super().Update(request, context)

    def Delete(self, request, context):
        return super().Delete(request, context)

    def Count(self, request, context):
        return super().Count(request, context)
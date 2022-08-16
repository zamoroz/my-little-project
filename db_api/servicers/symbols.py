from ..pb import symbols_pb2
from ..pb import symbols_pb2_grpc

class Symbols(symbols_pb2_grpc.SymbolsServicer):

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
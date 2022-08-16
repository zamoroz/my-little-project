from ..pb import wallet_pb2
from ..pb import wallet_pb2_grpc

class Wallet(wallet_pb2_grpc.WalletServicer):

    def Load(self, request, context):
        return super().Load(request, context)

    def Read(self, request, context):
        return super().Read(request, context)

    def Update(self, request, context):
        return super().Update(request, context)
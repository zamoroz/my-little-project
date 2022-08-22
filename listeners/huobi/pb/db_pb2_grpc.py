# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import db_pb2 as db__pb2


class ExchangesStub(object):
    """SERVICES
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/Exchanges/Create',
                request_serializer=db__pb2.ExchangeRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Read = channel.unary_unary(
                '/Exchanges/Read',
                request_serializer=db__pb2.ReadRequest.SerializeToString,
                response_deserializer=db__pb2.ExchangeRequest.FromString,
                )
        self.Update = channel.unary_unary(
                '/Exchanges/Update',
                request_serializer=db__pb2.ExchangeRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Delete = channel.unary_unary(
                '/Exchanges/Delete',
                request_serializer=db__pb2.ReadRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )


class ExchangesServicer(object):
    """SERVICES
    """

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExchangesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=db__pb2.ExchangeRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=db__pb2.ReadRequest.FromString,
                    response_serializer=db__pb2.ExchangeRequest.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=db__pb2.ExchangeRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=db__pb2.ReadRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Exchanges', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Exchanges(object):
    """SERVICES
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Exchanges/Create',
            db__pb2.ExchangeRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Exchanges/Read',
            db__pb2.ReadRequest.SerializeToString,
            db__pb2.ExchangeRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Exchanges/Update',
            db__pb2.ExchangeRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Exchanges/Delete',
            db__pb2.ReadRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class OrdersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/Orders/Create',
                request_serializer=db__pb2.ReadRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Add = channel.unary_unary(
                '/Orders/Add',
                request_serializer=db__pb2.OrderRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Read = channel.unary_unary(
                '/Orders/Read',
                request_serializer=db__pb2.ReadRequest.SerializeToString,
                response_deserializer=db__pb2.OrdersReply.FromString,
                )
        self.Update = channel.unary_unary(
                '/Orders/Update',
                request_serializer=db__pb2.OrderRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Delete = channel.unary_unary(
                '/Orders/Delete',
                request_serializer=db__pb2.DeleteOrder.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Count = channel.unary_unary(
                '/Orders/Count',
                request_serializer=db__pb2.ReadRequest.SerializeToString,
                response_deserializer=db__pb2.CountReply.FromString,
                )


class OrdersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Count(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrdersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=db__pb2.ReadRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=db__pb2.OrderRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=db__pb2.ReadRequest.FromString,
                    response_serializer=db__pb2.OrdersReply.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=db__pb2.OrderRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=db__pb2.DeleteOrder.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Count': grpc.unary_unary_rpc_method_handler(
                    servicer.Count,
                    request_deserializer=db__pb2.ReadRequest.FromString,
                    response_serializer=db__pb2.CountReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Orders', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Orders(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Orders/Create',
            db__pb2.ReadRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Orders/Add',
            db__pb2.OrderRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Orders/Read',
            db__pb2.ReadRequest.SerializeToString,
            db__pb2.OrdersReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Orders/Update',
            db__pb2.OrderRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Orders/Delete',
            db__pb2.DeleteOrder.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Orders/Count',
            db__pb2.ReadRequest.SerializeToString,
            db__pb2.CountReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SymbolsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/Symbols/Create',
                request_serializer=db__pb2.SymbolRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Read = channel.unary_unary(
                '/Symbols/Read',
                request_serializer=db__pb2.ReadRequest.SerializeToString,
                response_deserializer=db__pb2.SymbolsReply.FromString,
                )
        self.Update = channel.unary_unary(
                '/Symbols/Update',
                request_serializer=db__pb2.SymbolRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Delete = channel.unary_unary(
                '/Symbols/Delete',
                request_serializer=db__pb2.DeleteSymbol.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Count = channel.unary_unary(
                '/Symbols/Count',
                request_serializer=db__pb2.ReadRequest.SerializeToString,
                response_deserializer=db__pb2.CountReply.FromString,
                )


class SymbolsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Count(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SymbolsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=db__pb2.SymbolRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=db__pb2.ReadRequest.FromString,
                    response_serializer=db__pb2.SymbolsReply.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=db__pb2.SymbolRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=db__pb2.DeleteSymbol.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Count': grpc.unary_unary_rpc_method_handler(
                    servicer.Count,
                    request_deserializer=db__pb2.ReadRequest.FromString,
                    response_serializer=db__pb2.CountReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Symbols', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Symbols(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Symbols/Create',
            db__pb2.SymbolRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Symbols/Read',
            db__pb2.ReadRequest.SerializeToString,
            db__pb2.SymbolsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Symbols/Update',
            db__pb2.SymbolRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Symbols/Delete',
            db__pb2.DeleteSymbol.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Symbols/Count',
            db__pb2.ReadRequest.SerializeToString,
            db__pb2.CountReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class WalletStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/Wallet/Create',
                request_serializer=db__pb2.ReadRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )
        self.Read = channel.unary_unary(
                '/Wallet/Read',
                request_serializer=db__pb2.ReadRequest.SerializeToString,
                response_deserializer=db__pb2.WalletReply.FromString,
                )
        self.Update = channel.unary_unary(
                '/Wallet/Update',
                request_serializer=db__pb2.WalletRequest.SerializeToString,
                response_deserializer=db__pb2.CommonReply.FromString,
                )


class WalletServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WalletServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=db__pb2.ReadRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=db__pb2.ReadRequest.FromString,
                    response_serializer=db__pb2.WalletReply.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=db__pb2.WalletRequest.FromString,
                    response_serializer=db__pb2.CommonReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Wallet', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Wallet(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Wallet/Create',
            db__pb2.ReadRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Wallet/Read',
            db__pb2.ReadRequest.SerializeToString,
            db__pb2.WalletReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Wallet/Update',
            db__pb2.WalletRequest.SerializeToString,
            db__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from a3protos import a3Servicer_pb2 as a3protos_dot_a3Servicer__pb2


class a3ServicerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/protos.a3Servicer/CreateBook',
                request_serializer=a3protos_dot_a3Servicer__pb2.CreateBookRequest.SerializeToString,
                response_deserializer=a3protos_dot_a3Servicer__pb2.CreateBookResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/protos.a3Servicer/GetBook',
                request_serializer=a3protos_dot_a3Servicer__pb2.GetBookRequest.SerializeToString,
                response_deserializer=a3protos_dot_a3Servicer__pb2.GetBookResponse.FromString,
                )


class a3ServicerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_a3ServicerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=a3protos_dot_a3Servicer__pb2.CreateBookRequest.FromString,
                    response_serializer=a3protos_dot_a3Servicer__pb2.CreateBookResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=a3protos_dot_a3Servicer__pb2.GetBookRequest.FromString,
                    response_serializer=a3protos_dot_a3Servicer__pb2.GetBookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.a3Servicer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class a3Servicer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.a3Servicer/CreateBook',
            a3protos_dot_a3Servicer__pb2.CreateBookRequest.SerializeToString,
            a3protos_dot_a3Servicer__pb2.CreateBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.a3Servicer/GetBook',
            a3protos_dot_a3Servicer__pb2.GetBookRequest.SerializeToString,
            a3protos_dot_a3Servicer__pb2.GetBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
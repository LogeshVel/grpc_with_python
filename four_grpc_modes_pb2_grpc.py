# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import four_grpc_modes_pb2 as four__grpc__modes__pb2


class FourModesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UnaryAPI = channel.unary_unary(
                '/FourModes/UnaryAPI',
                request_serializer=four__grpc__modes__pb2.Request.SerializeToString,
                response_deserializer=four__grpc__modes__pb2.Response.FromString,
                )
        self.ServerStreamingAPI = channel.unary_stream(
                '/FourModes/ServerStreamingAPI',
                request_serializer=four__grpc__modes__pb2.Request.SerializeToString,
                response_deserializer=four__grpc__modes__pb2.Response.FromString,
                )
        self.ClientStreamingAPI = channel.stream_unary(
                '/FourModes/ClientStreamingAPI',
                request_serializer=four__grpc__modes__pb2.Request.SerializeToString,
                response_deserializer=four__grpc__modes__pb2.Response.FromString,
                )
        self.BiDirectionalStreamingAPI = channel.stream_stream(
                '/FourModes/BiDirectionalStreamingAPI',
                request_serializer=four__grpc__modes__pb2.Request.SerializeToString,
                response_deserializer=four__grpc__modes__pb2.Response.FromString,
                )


class FourModesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UnaryAPI(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServerStreamingAPI(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientStreamingAPI(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BiDirectionalStreamingAPI(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FourModesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UnaryAPI': grpc.unary_unary_rpc_method_handler(
                    servicer.UnaryAPI,
                    request_deserializer=four__grpc__modes__pb2.Request.FromString,
                    response_serializer=four__grpc__modes__pb2.Response.SerializeToString,
            ),
            'ServerStreamingAPI': grpc.unary_stream_rpc_method_handler(
                    servicer.ServerStreamingAPI,
                    request_deserializer=four__grpc__modes__pb2.Request.FromString,
                    response_serializer=four__grpc__modes__pb2.Response.SerializeToString,
            ),
            'ClientStreamingAPI': grpc.stream_unary_rpc_method_handler(
                    servicer.ClientStreamingAPI,
                    request_deserializer=four__grpc__modes__pb2.Request.FromString,
                    response_serializer=four__grpc__modes__pb2.Response.SerializeToString,
            ),
            'BiDirectionalStreamingAPI': grpc.stream_stream_rpc_method_handler(
                    servicer.BiDirectionalStreamingAPI,
                    request_deserializer=four__grpc__modes__pb2.Request.FromString,
                    response_serializer=four__grpc__modes__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FourModes', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FourModes(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UnaryAPI(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FourModes/UnaryAPI',
            four__grpc__modes__pb2.Request.SerializeToString,
            four__grpc__modes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServerStreamingAPI(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/FourModes/ServerStreamingAPI',
            four__grpc__modes__pb2.Request.SerializeToString,
            four__grpc__modes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClientStreamingAPI(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/FourModes/ClientStreamingAPI',
            four__grpc__modes__pb2.Request.SerializeToString,
            four__grpc__modes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BiDirectionalStreamingAPI(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/FourModes/BiDirectionalStreamingAPI',
            four__grpc__modes__pb2.Request.SerializeToString,
            four__grpc__modes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

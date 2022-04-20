# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import sample_pb2 as proto_dot_sample__pb2


class SampleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloServer = channel.stream_stream(
                '/sample.SampleService/HelloServer',
                request_serializer=proto_dot_sample__pb2.HelloMessage.SerializeToString,
                response_deserializer=proto_dot_sample__pb2.ReplyMessage.FromString,
                )


class SampleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HelloServer(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SampleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloServer': grpc.stream_stream_rpc_method_handler(
                    servicer.HelloServer,
                    request_deserializer=proto_dot_sample__pb2.HelloMessage.FromString,
                    response_serializer=proto_dot_sample__pb2.ReplyMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sample.SampleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SampleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HelloServer(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/sample.SampleService/HelloServer',
            proto_dot_sample__pb2.HelloMessage.SerializeToString,
            proto_dot_sample__pb2.ReplyMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
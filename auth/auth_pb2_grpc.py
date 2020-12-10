# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import auth_pb2 as auth__pb2


class authStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetToken = channel.unary_unary(
                '/authService.auth/GetToken',
                request_serializer=auth__pb2.user_password_request.SerializeToString,
                response_deserializer=auth__pb2.token_answer.FromString,
                )
        self.CheckToken = channel.unary_unary(
                '/authService.auth/CheckToken',
                request_serializer=auth__pb2.check_token_request.SerializeToString,
                response_deserializer=auth__pb2.ok_answer.FromString,
                )
        self.RegisterUser = channel.unary_unary(
                '/authService.auth/RegisterUser',
                request_serializer=auth__pb2.user_password_request.SerializeToString,
                response_deserializer=auth__pb2.ok_answer.FromString,
                )


class authServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_authServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetToken,
                    request_deserializer=auth__pb2.user_password_request.FromString,
                    response_serializer=auth__pb2.token_answer.SerializeToString,
            ),
            'CheckToken': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckToken,
                    request_deserializer=auth__pb2.check_token_request.FromString,
                    response_serializer=auth__pb2.ok_answer.SerializeToString,
            ),
            'RegisterUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterUser,
                    request_deserializer=auth__pb2.user_password_request.FromString,
                    response_serializer=auth__pb2.ok_answer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'authService.auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class auth(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authService.auth/GetToken',
            auth__pb2.user_password_request.SerializeToString,
            auth__pb2.token_answer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authService.auth/CheckToken',
            auth__pb2.check_token_request.SerializeToString,
            auth__pb2.ok_answer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authService.auth/RegisterUser',
            auth__pb2.user_password_request.SerializeToString,
            auth__pb2.ok_answer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

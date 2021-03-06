# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='authService',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nauth.proto\x12\x0b\x61uthService\"5\n\x13UserPasswordRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\"\n\x11\x43heckTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\x1a\n\nUserAnswer\x12\x0c\n\x04user\x18\x01 \x01(\t\"\x1c\n\x0bTokenAnswer\x12\r\n\x05token\x18\x01 \x01(\t2\xe7\x01\n\x04\x61uth\x12H\n\x08GetToken\x12 .authService.UserPasswordRequest\x1a\x18.authService.TokenAnswer\"\x00\x12G\n\nCheckToken\x12\x1e.authService.CheckTokenRequest\x1a\x17.authService.UserAnswer\"\x00\x12L\n\x0cRegisterUser\x12 .authService.UserPasswordRequest\x1a\x18.authService.TokenAnswer\"\x00\x62\x06proto3'
)




_USERPASSWORDREQUEST = _descriptor.Descriptor(
  name='UserPasswordRequest',
  full_name='authService.UserPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='authService.UserPasswordRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='authService.UserPasswordRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=80,
)


_CHECKTOKENREQUEST = _descriptor.Descriptor(
  name='CheckTokenRequest',
  full_name='authService.CheckTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='authService.CheckTokenRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=116,
)


_USERANSWER = _descriptor.Descriptor(
  name='UserAnswer',
  full_name='authService.UserAnswer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='authService.UserAnswer.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=144,
)


_TOKENANSWER = _descriptor.Descriptor(
  name='TokenAnswer',
  full_name='authService.TokenAnswer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='authService.TokenAnswer.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=174,
)

DESCRIPTOR.message_types_by_name['UserPasswordRequest'] = _USERPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['CheckTokenRequest'] = _CHECKTOKENREQUEST
DESCRIPTOR.message_types_by_name['UserAnswer'] = _USERANSWER
DESCRIPTOR.message_types_by_name['TokenAnswer'] = _TOKENANSWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserPasswordRequest = _reflection.GeneratedProtocolMessageType('UserPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERPASSWORDREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:authService.UserPasswordRequest)
  })
_sym_db.RegisterMessage(UserPasswordRequest)

CheckTokenRequest = _reflection.GeneratedProtocolMessageType('CheckTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKTOKENREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:authService.CheckTokenRequest)
  })
_sym_db.RegisterMessage(CheckTokenRequest)

UserAnswer = _reflection.GeneratedProtocolMessageType('UserAnswer', (_message.Message,), {
  'DESCRIPTOR' : _USERANSWER,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:authService.UserAnswer)
  })
_sym_db.RegisterMessage(UserAnswer)

TokenAnswer = _reflection.GeneratedProtocolMessageType('TokenAnswer', (_message.Message,), {
  'DESCRIPTOR' : _TOKENANSWER,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:authService.TokenAnswer)
  })
_sym_db.RegisterMessage(TokenAnswer)



_AUTH = _descriptor.ServiceDescriptor(
  name='auth',
  full_name='authService.auth',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=177,
  serialized_end=408,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetToken',
    full_name='authService.auth.GetToken',
    index=0,
    containing_service=None,
    input_type=_USERPASSWORDREQUEST,
    output_type=_TOKENANSWER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckToken',
    full_name='authService.auth.CheckToken',
    index=1,
    containing_service=None,
    input_type=_CHECKTOKENREQUEST,
    output_type=_USERANSWER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterUser',
    full_name='authService.auth.RegisterUser',
    index=2,
    containing_service=None,
    input_type=_USERPASSWORDREQUEST,
    output_type=_TOKENANSWER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTH)

DESCRIPTOR.services_by_name['auth'] = _AUTH

# @@protoc_insertion_point(module_scope)

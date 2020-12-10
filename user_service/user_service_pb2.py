# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_service.proto',
  package='userService',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12user_service.proto\x12\x0buserService\"9\n\x15stock_to_user_request\x12\x0c\n\x04user\x18\x01 \x02(\t\x12\x12\n\nstock_code\x18\x02 \x02(\t\"\'\n\x17get_user_stocks_request\x12\x0c\n\x04user\x18\x01 \x02(\t\"\x18\n\x16get_all_stocks_request\"\x1e\n\tok_answer\x12\x11\n\tok_string\x18\x01 \x02(\t\"\x1d\n\x0cstock_answer\x12\r\n\x05\x63odes\x18\x01 \x03(\t2\xd5\x02\n\x0cuser_service\x12N\n\x0e\x41\x64\x64StockToUser\x12\".userService.stock_to_user_request\x1a\x16.userService.ok_answer\"\x00\x12S\n\x13RemoveStockFromUser\x12\".userService.stock_to_user_request\x1a\x16.userService.ok_answer\"\x00\x12N\n\tGetStocks\x12$.userService.get_user_stocks_request\x1a\x19.userService.stock_answer\"\x00\x12P\n\x0cGetAllStocks\x12#.userService.get_all_stocks_request\x1a\x19.userService.stock_answer\"\x00'
)




_STOCK_TO_USER_REQUEST = _descriptor.Descriptor(
  name='stock_to_user_request',
  full_name='userService.stock_to_user_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='userService.stock_to_user_request.user', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stock_code', full_name='userService.stock_to_user_request.stock_code', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=92,
)


_GET_USER_STOCKS_REQUEST = _descriptor.Descriptor(
  name='get_user_stocks_request',
  full_name='userService.get_user_stocks_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='userService.get_user_stocks_request.user', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=133,
)


_GET_ALL_STOCKS_REQUEST = _descriptor.Descriptor(
  name='get_all_stocks_request',
  full_name='userService.get_all_stocks_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=159,
)


_OK_ANSWER = _descriptor.Descriptor(
  name='ok_answer',
  full_name='userService.ok_answer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok_string', full_name='userService.ok_answer.ok_string', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=191,
)


_STOCK_ANSWER = _descriptor.Descriptor(
  name='stock_answer',
  full_name='userService.stock_answer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='codes', full_name='userService.stock_answer.codes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=222,
)

DESCRIPTOR.message_types_by_name['stock_to_user_request'] = _STOCK_TO_USER_REQUEST
DESCRIPTOR.message_types_by_name['get_user_stocks_request'] = _GET_USER_STOCKS_REQUEST
DESCRIPTOR.message_types_by_name['get_all_stocks_request'] = _GET_ALL_STOCKS_REQUEST
DESCRIPTOR.message_types_by_name['ok_answer'] = _OK_ANSWER
DESCRIPTOR.message_types_by_name['stock_answer'] = _STOCK_ANSWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

stock_to_user_request = _reflection.GeneratedProtocolMessageType('stock_to_user_request', (_message.Message,), {
  'DESCRIPTOR' : _STOCK_TO_USER_REQUEST,
  '__module__' : 'user_service_pb2'
  # @@protoc_insertion_point(class_scope:userService.stock_to_user_request)
  })
_sym_db.RegisterMessage(stock_to_user_request)

get_user_stocks_request = _reflection.GeneratedProtocolMessageType('get_user_stocks_request', (_message.Message,), {
  'DESCRIPTOR' : _GET_USER_STOCKS_REQUEST,
  '__module__' : 'user_service_pb2'
  # @@protoc_insertion_point(class_scope:userService.get_user_stocks_request)
  })
_sym_db.RegisterMessage(get_user_stocks_request)

get_all_stocks_request = _reflection.GeneratedProtocolMessageType('get_all_stocks_request', (_message.Message,), {
  'DESCRIPTOR' : _GET_ALL_STOCKS_REQUEST,
  '__module__' : 'user_service_pb2'
  # @@protoc_insertion_point(class_scope:userService.get_all_stocks_request)
  })
_sym_db.RegisterMessage(get_all_stocks_request)

ok_answer = _reflection.GeneratedProtocolMessageType('ok_answer', (_message.Message,), {
  'DESCRIPTOR' : _OK_ANSWER,
  '__module__' : 'user_service_pb2'
  # @@protoc_insertion_point(class_scope:userService.ok_answer)
  })
_sym_db.RegisterMessage(ok_answer)

stock_answer = _reflection.GeneratedProtocolMessageType('stock_answer', (_message.Message,), {
  'DESCRIPTOR' : _STOCK_ANSWER,
  '__module__' : 'user_service_pb2'
  # @@protoc_insertion_point(class_scope:userService.stock_answer)
  })
_sym_db.RegisterMessage(stock_answer)



_USER_SERVICE = _descriptor.ServiceDescriptor(
  name='user_service',
  full_name='userService.user_service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=225,
  serialized_end=566,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddStockToUser',
    full_name='userService.user_service.AddStockToUser',
    index=0,
    containing_service=None,
    input_type=_STOCK_TO_USER_REQUEST,
    output_type=_OK_ANSWER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveStockFromUser',
    full_name='userService.user_service.RemoveStockFromUser',
    index=1,
    containing_service=None,
    input_type=_STOCK_TO_USER_REQUEST,
    output_type=_OK_ANSWER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetStocks',
    full_name='userService.user_service.GetStocks',
    index=2,
    containing_service=None,
    input_type=_GET_USER_STOCKS_REQUEST,
    output_type=_STOCK_ANSWER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllStocks',
    full_name='userService.user_service.GetAllStocks',
    index=3,
    containing_service=None,
    input_type=_GET_ALL_STOCKS_REQUEST,
    output_type=_STOCK_ANSWER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER_SERVICE)

DESCRIPTOR.services_by_name['user_service'] = _USER_SERVICE

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: upollo/upollo_shadow.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aupollo/upollo_shadow.proto\x12\x06uwGrpc\"N\n\x07Library\x12\"\n\x08platform\x18\x01 \x01(\x0e\x32\x10.uwGrpc.Platform\x12\x11\n\titeration\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t*\xe0\x01\n\x08Platform\x12\x18\n\x14PLATFORM_UNSPECIFIED\x10\x00\x12\x17\n\x13PLATFORM_CLIENT_IOS\x10\x01\x12\x1b\n\x17PLATFORM_CLIENT_ANDROID\x10\x02\x12\x17\n\x13PLATFORM_CLIENT_WEB\x10\x03\x12\x1a\n\x16PLATFORM_SERVER_NODEJS\x10\n\x12\x16\n\x12PLATFORM_SERVER_GO\x10\x0b\x12\x1a\n\x16PLATFORM_SERVER_PYTHON\x10\x0c\x12\x1b\n\x17PLATFORM_WEBHOOK_STRIPE\x10\x64\x42I\n\x0e\x61i.upollo.grpcP\x01Z,github.com/userwatch/uw1/protos/uwgrpcshadow\xa2\x02\x06UwGrpcb\x06proto3')

_PLATFORM = DESCRIPTOR.enum_types_by_name['Platform']
Platform = enum_type_wrapper.EnumTypeWrapper(_PLATFORM)
PLATFORM_UNSPECIFIED = 0
PLATFORM_CLIENT_IOS = 1
PLATFORM_CLIENT_ANDROID = 2
PLATFORM_CLIENT_WEB = 3
PLATFORM_SERVER_NODEJS = 10
PLATFORM_SERVER_GO = 11
PLATFORM_SERVER_PYTHON = 12
PLATFORM_WEBHOOK_STRIPE = 100


_LIBRARY = DESCRIPTOR.message_types_by_name['Library']
Library = _reflection.GeneratedProtocolMessageType('Library', (_message.Message,), {
  'DESCRIPTOR' : _LIBRARY,
  '__module__' : 'upollo.upollo_shadow_pb2'
  # @@protoc_insertion_point(class_scope:uwGrpc.Library)
  })
_sym_db.RegisterMessage(Library)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016ai.upollo.grpcP\001Z,github.com/userwatch/uw1/protos/uwgrpcshadow\242\002\006UwGrpc'
  _PLATFORM._serialized_start=119
  _PLATFORM._serialized_end=343
  _LIBRARY._serialized_start=38
  _LIBRARY._serialized_end=116
# @@protoc_insertion_point(module_scope)

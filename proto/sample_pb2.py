# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/sample.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proto/sample.proto\x12\x06sample\")\n\x0cHelloMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\"!\n\x0cReplyMessage\x12\x11\n\treply_msg\x18\x01 \x01(\t2P\n\rSampleService\x12?\n\x0bHelloServer\x12\x14.sample.HelloMessage\x1a\x14.sample.ReplyMessage\"\x00(\x01\x30\x01\x62\x06proto3')



_HELLOMESSAGE = DESCRIPTOR.message_types_by_name['HelloMessage']
_REPLYMESSAGE = DESCRIPTOR.message_types_by_name['ReplyMessage']
HelloMessage = _reflection.GeneratedProtocolMessageType('HelloMessage', (_message.Message,), {
  'DESCRIPTOR' : _HELLOMESSAGE,
  '__module__' : 'proto.sample_pb2'
  # @@protoc_insertion_point(class_scope:sample.HelloMessage)
  })
_sym_db.RegisterMessage(HelloMessage)

ReplyMessage = _reflection.GeneratedProtocolMessageType('ReplyMessage', (_message.Message,), {
  'DESCRIPTOR' : _REPLYMESSAGE,
  '__module__' : 'proto.sample_pb2'
  # @@protoc_insertion_point(class_scope:sample.ReplyMessage)
  })
_sym_db.RegisterMessage(ReplyMessage)

_SAMPLESERVICE = DESCRIPTOR.services_by_name['SampleService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOMESSAGE._serialized_start=30
  _HELLOMESSAGE._serialized_end=71
  _REPLYMESSAGE._serialized_start=73
  _REPLYMESSAGE._serialized_end=106
  _SAMPLESERVICE._serialized_start=108
  _SAMPLESERVICE._serialized_end=188
# @@protoc_insertion_point(module_scope)

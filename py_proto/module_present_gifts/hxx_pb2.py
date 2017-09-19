# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_present_gifts.hxx

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import module_scene.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='module_present_gifts.hxx',
  package='',
  serialized_pb=_b('\n\x18module_present_gifts.hxx\x1a\x10module_scene.hxx\"W\n\x1bPBMsgC2SPresentGiftsRequest\x12\x13\n\x0broleid_recv\x18\x01 \x01(\x05\x12\x0f\n\x07gift_id\x18\x02 \x01(\x05\x12\x12\n\ngift_count\x18\x03 \x01(\x05\"\x82\x01\n\x1cPBMsgS2CPresentGiftsResponse\x12\x0f\n\x07gift_id\x18\x01 \x01(\x05\x12)\n\x0erole_recv_data\x18\x02 \x01(\x0b\x32\x11.PBPlayerMainData\x12\x14\n\x0crelationship\x18\x03 \x01(\x05\x12\x10\n\x08ret_code\x18\x04 \x01(\x05*c\n\x1aMSGID_MODULE_PRESENT_GIFTS\x12!\n\x1cID_C2S_PRESENT_GIFTS_REQUEST\x10\x80\x42\x12\"\n\x1dID_C2S_PRESENT_GIFTS_RESPONSE\x10\x81\x42\x42\x02H\x01')
  ,
  dependencies=[module_scene.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGID_MODULE_PRESENT_GIFTS = _descriptor.EnumDescriptor(
  name='MSGID_MODULE_PRESENT_GIFTS',
  full_name='MSGID_MODULE_PRESENT_GIFTS',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_PRESENT_GIFTS_REQUEST', index=0, number=8448,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_PRESENT_GIFTS_RESPONSE', index=1, number=8449,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=268,
  serialized_end=367,
)
_sym_db.RegisterEnumDescriptor(_MSGID_MODULE_PRESENT_GIFTS)

MSGID_MODULE_PRESENT_GIFTS = enum_type_wrapper.EnumTypeWrapper(_MSGID_MODULE_PRESENT_GIFTS)
ID_C2S_PRESENT_GIFTS_REQUEST = 8448
ID_C2S_PRESENT_GIFTS_RESPONSE = 8449



_PBMSGC2SPRESENTGIFTSREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SPresentGiftsRequest',
  full_name='PBMsgC2SPresentGiftsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleid_recv', full_name='PBMsgC2SPresentGiftsRequest.roleid_recv', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='PBMsgC2SPresentGiftsRequest.gift_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_count', full_name='PBMsgC2SPresentGiftsRequest.gift_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=133,
)


_PBMSGS2CPRESENTGIFTSRESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CPresentGiftsResponse',
  full_name='PBMsgS2CPresentGiftsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='PBMsgS2CPresentGiftsResponse.gift_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_recv_data', full_name='PBMsgS2CPresentGiftsResponse.role_recv_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship', full_name='PBMsgS2CPresentGiftsResponse.relationship', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgS2CPresentGiftsResponse.ret_code', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=266,
)

_PBMSGS2CPRESENTGIFTSRESPONSE.fields_by_name['role_recv_data'].message_type = module_scene.hxx_pb2._PBPLAYERMAINDATA
DESCRIPTOR.message_types_by_name['PBMsgC2SPresentGiftsRequest'] = _PBMSGC2SPRESENTGIFTSREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CPresentGiftsResponse'] = _PBMSGS2CPRESENTGIFTSRESPONSE
DESCRIPTOR.enum_types_by_name['MSGID_MODULE_PRESENT_GIFTS'] = _MSGID_MODULE_PRESENT_GIFTS

PBMsgC2SPresentGiftsRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SPresentGiftsRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SPRESENTGIFTSREQUEST,
  __module__ = 'module_present_gifts.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SPresentGiftsRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SPresentGiftsRequest)

PBMsgS2CPresentGiftsResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CPresentGiftsResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CPRESENTGIFTSRESPONSE,
  __module__ = 'module_present_gifts.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CPresentGiftsResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CPresentGiftsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_furnance.hxx

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


import module_props.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='module_furnance.hxx',
  package='',
  serialized_pb=_b('\n\x13module_furnance.hxx\x1a\x10module_props.hxx\"S\n\x18PBMsgC2SEquipFuseRequest\x12*\n\tpack_type\x18\x01 \x01(\x0e\x32\n.EPackType:\x0b\x45_PACK_MAIN\x12\x0b\n\x03pos\x18\x02 \x03(\x05\",\n\x19PBMsgS2CEquipFuseResponse\x12\x0f\n\x07retcode\x18\x01 \x01(\x05*\x94\x01\n\x15MSGID_MODULE_FURNANCE\x12\x1d\n\x18ID_MODULE_FURNANCE_BEGIN\x10\x80(\x12\x1e\n\x19ID_C2S_EQUIP_FUSE_REQUEST\x10\x81(\x12\x1f\n\x1aID_S2C_EQUIP_FUSE_RESPONSE\x10\x82(\x12\x1b\n\x16ID_MODULE_FURNANCE_END\x10\xff)B\x02H\x01')
  ,
  dependencies=[module_props.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGID_MODULE_FURNANCE = _descriptor.EnumDescriptor(
  name='MSGID_MODULE_FURNANCE',
  full_name='MSGID_MODULE_FURNANCE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ID_MODULE_FURNANCE_BEGIN', index=0, number=5120,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_EQUIP_FUSE_REQUEST', index=1, number=5121,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_EQUIP_FUSE_RESPONSE', index=2, number=5122,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_MODULE_FURNANCE_END', index=3, number=5375,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=173,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_MSGID_MODULE_FURNANCE)

MSGID_MODULE_FURNANCE = enum_type_wrapper.EnumTypeWrapper(_MSGID_MODULE_FURNANCE)
ID_MODULE_FURNANCE_BEGIN = 5120
ID_C2S_EQUIP_FUSE_REQUEST = 5121
ID_S2C_EQUIP_FUSE_RESPONSE = 5122
ID_MODULE_FURNANCE_END = 5375



_PBMSGC2SEQUIPFUSEREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SEquipFuseRequest',
  full_name='PBMsgC2SEquipFuseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pack_type', full_name='PBMsgC2SEquipFuseRequest.pack_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos', full_name='PBMsgC2SEquipFuseRequest.pos', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=41,
  serialized_end=124,
)


_PBMSGS2CEQUIPFUSERESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CEquipFuseResponse',
  full_name='PBMsgS2CEquipFuseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retcode', full_name='PBMsgS2CEquipFuseResponse.retcode', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=126,
  serialized_end=170,
)

_PBMSGC2SEQUIPFUSEREQUEST.fields_by_name['pack_type'].enum_type = module_props.hxx_pb2._EPACKTYPE
DESCRIPTOR.message_types_by_name['PBMsgC2SEquipFuseRequest'] = _PBMSGC2SEQUIPFUSEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CEquipFuseResponse'] = _PBMSGS2CEQUIPFUSERESPONSE
DESCRIPTOR.enum_types_by_name['MSGID_MODULE_FURNANCE'] = _MSGID_MODULE_FURNANCE

PBMsgC2SEquipFuseRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SEquipFuseRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SEQUIPFUSEREQUEST,
  __module__ = 'module_furnance.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SEquipFuseRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SEquipFuseRequest)

PBMsgS2CEquipFuseResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CEquipFuseResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CEQUIPFUSERESPONSE,
  __module__ = 'module_furnance.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CEquipFuseResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CEquipFuseResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
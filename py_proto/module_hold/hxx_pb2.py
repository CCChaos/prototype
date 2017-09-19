# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_hold.hxx

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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='module_hold.hxx',
  package='',
  serialized_pb=_b('\n\x0fmodule_hold.hxx\"(\n\x13PBMsgC2SHoldRequest\x12\x11\n\ttarget_id\x18\x01 \x01(\x05\":\n\x14PBMsgS2CHoldResponse\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x11\n\ttarget_id\x18\x02 \x01(\x05\"?\n\x19PBMsgS2CHoldRequestNotify\x12\x0f\n\x07role_id\x18\x01 \x01(\x05\x12\x11\n\trole_name\x18\x02 \x01(\t\"9\n\x15PBMsgS2CHoldAckNotify\x12\x11\n\trole_name\x18\x01 \x01(\t\x12\r\n\x05\x61gree\x18\x02 \x01(\x08\"8\n\x16PBMsgC2SHoldAckRequest\x12\r\n\x05\x61gree\x18\x01 \x01(\x08\x12\x0f\n\x07role_id\x18\x02 \x01(\x05\"Q\n\x17PBMsgS2CHoldAckResponse\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x12\n\nhold_state\x18\x02 \x01(\x05\x12\x11\n\ttarget_id\x18\x03 \x01(\x05\",\n\x17PBMsgC2SHoldDownRequest\x12\x11\n\tdown_type\x18\x01 \x01(\x05\"+\n\x18PBMsgS2CHoldDownResponse\x12\x0f\n\x07retcode\x18\x01 \x01(\x05*\x82\x02\n\x11MSGID_MODULE_HOLD\x12\x18\n\x13ID_C2S_HOLD_REQUEST\x10\x80\x46\x12\x19\n\x14ID_S2C_HOLD_RESPONSE\x10\x81\x46\x12\x1f\n\x1aID_S2C_HOLD_REQUEST_NOTIFY\x10\x82\x46\x12\x1c\n\x17ID_C2S_HOLD_ACK_REQUEST\x10\x83\x46\x12\x1d\n\x18ID_S2C_HOLD_ACK_RESPONSE\x10\x84\x46\x12\x1b\n\x16ID_S2C_HOLD_ACK_NOTIFY\x10\x85\x46\x12\x1d\n\x18ID_C2S_HOLD_DOWN_REQUEST\x10\x86\x46\x12\x1e\n\x19ID_S2C_HOLD_DOWN_RESPONSE\x10\x87\x46*P\n\tEHoldType\x12\x13\n\x0fHOLD_TYPE_NONDE\x10\x00\x12\x14\n\x10HOLD_TYPE_NORMAL\x10\x01\x12\x18\n\x14HOLD_TYPE_XIAOSHIMEI\x10\x02*T\n\nEHoldState\x12\x13\n\x0fHOLD_STATE_NONE\x10\x00\x12\x19\n\x15HOLD_STATE_HOLD_OTHER\x10\x01\x12\x16\n\x12HOLD_STATE_BE_HOLD\x10\x02\x42\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGID_MODULE_HOLD = _descriptor.EnumDescriptor(
  name='MSGID_MODULE_HOLD',
  full_name='MSGID_MODULE_HOLD',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_HOLD_REQUEST', index=0, number=8960,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_HOLD_RESPONSE', index=1, number=8961,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_HOLD_REQUEST_NOTIFY', index=2, number=8962,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_HOLD_ACK_REQUEST', index=3, number=8963,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_HOLD_ACK_RESPONSE', index=4, number=8964,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_HOLD_ACK_NOTIFY', index=5, number=8965,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_HOLD_DOWN_REQUEST', index=6, number=8966,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_HOLD_DOWN_RESPONSE', index=7, number=8967,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=478,
  serialized_end=736,
)
_sym_db.RegisterEnumDescriptor(_MSGID_MODULE_HOLD)

MSGID_MODULE_HOLD = enum_type_wrapper.EnumTypeWrapper(_MSGID_MODULE_HOLD)
_EHOLDTYPE = _descriptor.EnumDescriptor(
  name='EHoldType',
  full_name='EHoldType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HOLD_TYPE_NONDE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLD_TYPE_NORMAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLD_TYPE_XIAOSHIMEI', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=738,
  serialized_end=818,
)
_sym_db.RegisterEnumDescriptor(_EHOLDTYPE)

EHoldType = enum_type_wrapper.EnumTypeWrapper(_EHOLDTYPE)
_EHOLDSTATE = _descriptor.EnumDescriptor(
  name='EHoldState',
  full_name='EHoldState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HOLD_STATE_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLD_STATE_HOLD_OTHER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLD_STATE_BE_HOLD', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=820,
  serialized_end=904,
)
_sym_db.RegisterEnumDescriptor(_EHOLDSTATE)

EHoldState = enum_type_wrapper.EnumTypeWrapper(_EHOLDSTATE)
ID_C2S_HOLD_REQUEST = 8960
ID_S2C_HOLD_RESPONSE = 8961
ID_S2C_HOLD_REQUEST_NOTIFY = 8962
ID_C2S_HOLD_ACK_REQUEST = 8963
ID_S2C_HOLD_ACK_RESPONSE = 8964
ID_S2C_HOLD_ACK_NOTIFY = 8965
ID_C2S_HOLD_DOWN_REQUEST = 8966
ID_S2C_HOLD_DOWN_RESPONSE = 8967
HOLD_TYPE_NONDE = 0
HOLD_TYPE_NORMAL = 1
HOLD_TYPE_XIAOSHIMEI = 2
HOLD_STATE_NONE = 0
HOLD_STATE_HOLD_OTHER = 1
HOLD_STATE_BE_HOLD = 2



_PBMSGC2SHOLDREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SHoldRequest',
  full_name='PBMsgC2SHoldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_id', full_name='PBMsgC2SHoldRequest.target_id', index=0,
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
  serialized_start=19,
  serialized_end=59,
)


_PBMSGS2CHOLDRESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CHoldResponse',
  full_name='PBMsgS2CHoldResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retcode', full_name='PBMsgS2CHoldResponse.retcode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='PBMsgS2CHoldResponse.target_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=61,
  serialized_end=119,
)


_PBMSGS2CHOLDREQUESTNOTIFY = _descriptor.Descriptor(
  name='PBMsgS2CHoldRequestNotify',
  full_name='PBMsgS2CHoldRequestNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgS2CHoldRequestNotify.role_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_name', full_name='PBMsgS2CHoldRequestNotify.role_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=121,
  serialized_end=184,
)


_PBMSGS2CHOLDACKNOTIFY = _descriptor.Descriptor(
  name='PBMsgS2CHoldAckNotify',
  full_name='PBMsgS2CHoldAckNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_name', full_name='PBMsgS2CHoldAckNotify.role_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agree', full_name='PBMsgS2CHoldAckNotify.agree', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=186,
  serialized_end=243,
)


_PBMSGC2SHOLDACKREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SHoldAckRequest',
  full_name='PBMsgC2SHoldAckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agree', full_name='PBMsgC2SHoldAckRequest.agree', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgC2SHoldAckRequest.role_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=245,
  serialized_end=301,
)


_PBMSGS2CHOLDACKRESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CHoldAckResponse',
  full_name='PBMsgS2CHoldAckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retcode', full_name='PBMsgS2CHoldAckResponse.retcode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hold_state', full_name='PBMsgS2CHoldAckResponse.hold_state', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='PBMsgS2CHoldAckResponse.target_id', index=2,
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
  serialized_start=303,
  serialized_end=384,
)


_PBMSGC2SHOLDDOWNREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SHoldDownRequest',
  full_name='PBMsgC2SHoldDownRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='down_type', full_name='PBMsgC2SHoldDownRequest.down_type', index=0,
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
  serialized_start=386,
  serialized_end=430,
)


_PBMSGS2CHOLDDOWNRESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CHoldDownResponse',
  full_name='PBMsgS2CHoldDownResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retcode', full_name='PBMsgS2CHoldDownResponse.retcode', index=0,
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
  serialized_start=432,
  serialized_end=475,
)

DESCRIPTOR.message_types_by_name['PBMsgC2SHoldRequest'] = _PBMSGC2SHOLDREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CHoldResponse'] = _PBMSGS2CHOLDRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgS2CHoldRequestNotify'] = _PBMSGS2CHOLDREQUESTNOTIFY
DESCRIPTOR.message_types_by_name['PBMsgS2CHoldAckNotify'] = _PBMSGS2CHOLDACKNOTIFY
DESCRIPTOR.message_types_by_name['PBMsgC2SHoldAckRequest'] = _PBMSGC2SHOLDACKREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CHoldAckResponse'] = _PBMSGS2CHOLDACKRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgC2SHoldDownRequest'] = _PBMSGC2SHOLDDOWNREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CHoldDownResponse'] = _PBMSGS2CHOLDDOWNRESPONSE
DESCRIPTOR.enum_types_by_name['MSGID_MODULE_HOLD'] = _MSGID_MODULE_HOLD
DESCRIPTOR.enum_types_by_name['EHoldType'] = _EHOLDTYPE
DESCRIPTOR.enum_types_by_name['EHoldState'] = _EHOLDSTATE

PBMsgC2SHoldRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SHoldRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SHOLDREQUEST,
  __module__ = 'module_hold.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SHoldRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SHoldRequest)

PBMsgS2CHoldResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CHoldResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CHOLDRESPONSE,
  __module__ = 'module_hold.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CHoldResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CHoldResponse)

PBMsgS2CHoldRequestNotify = _reflection.GeneratedProtocolMessageType('PBMsgS2CHoldRequestNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CHOLDREQUESTNOTIFY,
  __module__ = 'module_hold.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CHoldRequestNotify)
  ))
_sym_db.RegisterMessage(PBMsgS2CHoldRequestNotify)

PBMsgS2CHoldAckNotify = _reflection.GeneratedProtocolMessageType('PBMsgS2CHoldAckNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CHOLDACKNOTIFY,
  __module__ = 'module_hold.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CHoldAckNotify)
  ))
_sym_db.RegisterMessage(PBMsgS2CHoldAckNotify)

PBMsgC2SHoldAckRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SHoldAckRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SHOLDACKREQUEST,
  __module__ = 'module_hold.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SHoldAckRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SHoldAckRequest)

PBMsgS2CHoldAckResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CHoldAckResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CHOLDACKRESPONSE,
  __module__ = 'module_hold.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CHoldAckResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CHoldAckResponse)

PBMsgC2SHoldDownRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SHoldDownRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SHOLDDOWNREQUEST,
  __module__ = 'module_hold.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SHoldDownRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SHoldDownRequest)

PBMsgS2CHoldDownResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CHoldDownResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CHOLDDOWNRESPONSE,
  __module__ = 'module_hold.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CHoldDownResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CHoldDownResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

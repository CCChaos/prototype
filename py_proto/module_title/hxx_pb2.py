# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_title.hxx

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
  name='module_title.hxx',
  package='',
  serialized_pb=_b('\n\x10module_title.hxx\"%\n\x11PBC2STitleRequest\x12\x10\n\x08title_id\x18\x01 \x01(\x05\"8\n\x12PBS2CTitleResponse\x12\x10\n\x08title_id\x18\x01 \x01(\x05\x12\x10\n\x08ret_code\x18\x03 \x01(\x05\"7\n\x0fPBRoleTitleNode\x12\x10\n\x08title_id\x18\x01 \x01(\x05\x12\x12\n\ntitle_time\x18\x02 \x01(\x05\"i\n\x12PBS2CRoleTitleList\x12)\n\x0frole_title_list\x18\x01 \x03(\x0b\x32\x10.PBRoleTitleNode\x12\x14\n\x0c\x63hoose_title\x18\x02 \x01(\x05\x12\x12\n\nwear_title\x18\x04 \x01(\x05\"=\n\x16PBS2CAddNewTitleNotify\x12#\n\tnew_title\x18\x01 \x01(\x0b\x32\x10.PBRoleTitleNode\"0\n\x17PBS2CDelTitleListNotify\x12\x15\n\rtitle_id_list\x18\x01 \x03(\x05*\xe3\x02\n\x12MSGID_MODULE_TITEL\x12\x18\n\x13ID_S2C_TITLE_NOTIFY\x10\x80H\x12\x1e\n\x19ID_C2S_WEAR_TITLE_REQUEST\x10\x81H\x12\x1f\n\x1aID_S2C_WEAR_TITLE_RESPONSE\x10\x82H\x12 \n\x1bID_C2S_UNWEAR_TITLE_REQUEST\x10\x83H\x12!\n\x1cID_S2C_UNWEAR_TITLE_RESPONSE\x10\x84H\x12 \n\x1bID_C2S_CHOOSE_TITLE_REQUEST\x10\x85H\x12!\n\x1cID_S2C_CHOOSE_TITLE_RESPONSE\x10\x86H\x12\"\n\x1dID_C2S_UNCHOOSE_TITLE_REQUEST\x10\x87H\x12#\n\x1eID_S2C_UNCHOOSE_TITLE_RESPONSE\x10\x88H\x12\x1f\n\x1aID_S2C_DELETE_TITLE_NOTIFY\x10\x89H*\xc6\x01\n\x0f\x45TitleRangeType\x12&\n\"TITLE_CHARM_RANGE_TYPE_FULLSERVICE\x10\x01\x12\x1f\n\x1bTITLE_CHARM_RANGE_TYPE_CAMP\x10\x02\x12 \n\x1cTITLE_CHARM_RANGE_TYPE_GUILD\x10\x03\x12$\n TITLE_CHARM_RANGE_TYPE_OCCUPATIO\x10\x04\x12\"\n\x1eTITLE_CHARM_RANGE_TYPE_GENERAL\x10\x05\x42\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGID_MODULE_TITEL = _descriptor.EnumDescriptor(
  name='MSGID_MODULE_TITEL',
  full_name='MSGID_MODULE_TITEL',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_TITLE_NOTIFY', index=0, number=9216,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_WEAR_TITLE_REQUEST', index=1, number=9217,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_WEAR_TITLE_RESPONSE', index=2, number=9218,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_UNWEAR_TITLE_REQUEST', index=3, number=9219,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_UNWEAR_TITLE_RESPONSE', index=4, number=9220,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_CHOOSE_TITLE_REQUEST', index=5, number=9221,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_CHOOSE_TITLE_RESPONSE', index=6, number=9222,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_UNCHOOSE_TITLE_REQUEST', index=7, number=9223,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_UNCHOOSE_TITLE_RESPONSE', index=8, number=9224,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_DELETE_TITLE_NOTIFY', index=9, number=9225,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=395,
  serialized_end=750,
)
_sym_db.RegisterEnumDescriptor(_MSGID_MODULE_TITEL)

MSGID_MODULE_TITEL = enum_type_wrapper.EnumTypeWrapper(_MSGID_MODULE_TITEL)
_ETITLERANGETYPE = _descriptor.EnumDescriptor(
  name='ETitleRangeType',
  full_name='ETitleRangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TITLE_CHARM_RANGE_TYPE_FULLSERVICE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TITLE_CHARM_RANGE_TYPE_CAMP', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TITLE_CHARM_RANGE_TYPE_GUILD', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TITLE_CHARM_RANGE_TYPE_OCCUPATIO', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TITLE_CHARM_RANGE_TYPE_GENERAL', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=753,
  serialized_end=951,
)
_sym_db.RegisterEnumDescriptor(_ETITLERANGETYPE)

ETitleRangeType = enum_type_wrapper.EnumTypeWrapper(_ETITLERANGETYPE)
ID_S2C_TITLE_NOTIFY = 9216
ID_C2S_WEAR_TITLE_REQUEST = 9217
ID_S2C_WEAR_TITLE_RESPONSE = 9218
ID_C2S_UNWEAR_TITLE_REQUEST = 9219
ID_S2C_UNWEAR_TITLE_RESPONSE = 9220
ID_C2S_CHOOSE_TITLE_REQUEST = 9221
ID_S2C_CHOOSE_TITLE_RESPONSE = 9222
ID_C2S_UNCHOOSE_TITLE_REQUEST = 9223
ID_S2C_UNCHOOSE_TITLE_RESPONSE = 9224
ID_S2C_DELETE_TITLE_NOTIFY = 9225
TITLE_CHARM_RANGE_TYPE_FULLSERVICE = 1
TITLE_CHARM_RANGE_TYPE_CAMP = 2
TITLE_CHARM_RANGE_TYPE_GUILD = 3
TITLE_CHARM_RANGE_TYPE_OCCUPATIO = 4
TITLE_CHARM_RANGE_TYPE_GENERAL = 5



_PBC2STITLEREQUEST = _descriptor.Descriptor(
  name='PBC2STitleRequest',
  full_name='PBC2STitleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title_id', full_name='PBC2STitleRequest.title_id', index=0,
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
  serialized_start=20,
  serialized_end=57,
)


_PBS2CTITLERESPONSE = _descriptor.Descriptor(
  name='PBS2CTitleResponse',
  full_name='PBS2CTitleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title_id', full_name='PBS2CTitleResponse.title_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBS2CTitleResponse.ret_code', index=1,
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
  serialized_start=59,
  serialized_end=115,
)


_PBROLETITLENODE = _descriptor.Descriptor(
  name='PBRoleTitleNode',
  full_name='PBRoleTitleNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title_id', full_name='PBRoleTitleNode.title_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title_time', full_name='PBRoleTitleNode.title_time', index=1,
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
  serialized_start=117,
  serialized_end=172,
)


_PBS2CROLETITLELIST = _descriptor.Descriptor(
  name='PBS2CRoleTitleList',
  full_name='PBS2CRoleTitleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_title_list', full_name='PBS2CRoleTitleList.role_title_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='choose_title', full_name='PBS2CRoleTitleList.choose_title', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wear_title', full_name='PBS2CRoleTitleList.wear_title', index=2,
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
  serialized_start=174,
  serialized_end=279,
)


_PBS2CADDNEWTITLENOTIFY = _descriptor.Descriptor(
  name='PBS2CAddNewTitleNotify',
  full_name='PBS2CAddNewTitleNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_title', full_name='PBS2CAddNewTitleNotify.new_title', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=281,
  serialized_end=342,
)


_PBS2CDELTITLELISTNOTIFY = _descriptor.Descriptor(
  name='PBS2CDelTitleListNotify',
  full_name='PBS2CDelTitleListNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title_id_list', full_name='PBS2CDelTitleListNotify.title_id_list', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=344,
  serialized_end=392,
)

_PBS2CROLETITLELIST.fields_by_name['role_title_list'].message_type = _PBROLETITLENODE
_PBS2CADDNEWTITLENOTIFY.fields_by_name['new_title'].message_type = _PBROLETITLENODE
DESCRIPTOR.message_types_by_name['PBC2STitleRequest'] = _PBC2STITLEREQUEST
DESCRIPTOR.message_types_by_name['PBS2CTitleResponse'] = _PBS2CTITLERESPONSE
DESCRIPTOR.message_types_by_name['PBRoleTitleNode'] = _PBROLETITLENODE
DESCRIPTOR.message_types_by_name['PBS2CRoleTitleList'] = _PBS2CROLETITLELIST
DESCRIPTOR.message_types_by_name['PBS2CAddNewTitleNotify'] = _PBS2CADDNEWTITLENOTIFY
DESCRIPTOR.message_types_by_name['PBS2CDelTitleListNotify'] = _PBS2CDELTITLELISTNOTIFY
DESCRIPTOR.enum_types_by_name['MSGID_MODULE_TITEL'] = _MSGID_MODULE_TITEL
DESCRIPTOR.enum_types_by_name['ETitleRangeType'] = _ETITLERANGETYPE

PBC2STitleRequest = _reflection.GeneratedProtocolMessageType('PBC2STitleRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBC2STITLEREQUEST,
  __module__ = 'module_title.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBC2STitleRequest)
  ))
_sym_db.RegisterMessage(PBC2STitleRequest)

PBS2CTitleResponse = _reflection.GeneratedProtocolMessageType('PBS2CTitleResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBS2CTITLERESPONSE,
  __module__ = 'module_title.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBS2CTitleResponse)
  ))
_sym_db.RegisterMessage(PBS2CTitleResponse)

PBRoleTitleNode = _reflection.GeneratedProtocolMessageType('PBRoleTitleNode', (_message.Message,), dict(
  DESCRIPTOR = _PBROLETITLENODE,
  __module__ = 'module_title.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBRoleTitleNode)
  ))
_sym_db.RegisterMessage(PBRoleTitleNode)

PBS2CRoleTitleList = _reflection.GeneratedProtocolMessageType('PBS2CRoleTitleList', (_message.Message,), dict(
  DESCRIPTOR = _PBS2CROLETITLELIST,
  __module__ = 'module_title.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBS2CRoleTitleList)
  ))
_sym_db.RegisterMessage(PBS2CRoleTitleList)

PBS2CAddNewTitleNotify = _reflection.GeneratedProtocolMessageType('PBS2CAddNewTitleNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBS2CADDNEWTITLENOTIFY,
  __module__ = 'module_title.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBS2CAddNewTitleNotify)
  ))
_sym_db.RegisterMessage(PBS2CAddNewTitleNotify)

PBS2CDelTitleListNotify = _reflection.GeneratedProtocolMessageType('PBS2CDelTitleListNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBS2CDELTITLELISTNOTIFY,
  __module__ = 'module_title.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBS2CDelTitleListNotify)
  ))
_sym_db.RegisterMessage(PBS2CDelTitleListNotify)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
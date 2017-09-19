# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_count.hxx

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
  name='module_count.hxx',
  package='',
  serialized_pb=_b('\n\x10module_count.hxx\"E\n\rPBCounterInfo\x12\x12\n\ncounter_id\x18\x01 \x01(\x04\x12\r\n\x05times\x18\x02 \x01(\r\x12\x11\n\tbuy_times\x18\x03 \x01(\r\"3\n\x0bPBCountData\x12$\n\x0c\x63ounter_info\x18\x01 \x03(\x0b\x32\x0e.PBCounterInfo\"n\n\x07PBCount\x12\x30\n\ncount_type\x18\x01 \x01(\x0e\x32\x0e.EnCounterType:\x0c\x43OUNTER_NONE\x12\x10\n\x08\x63ount_id\x18\x02 \x01(\x05\x12\x10\n\x08max_time\x18\x03 \x01(\x05\x12\r\n\x05times\x18\x04 \x01(\x05\"4\n\x14PBS2CRoleCountNofity\x12\x1c\n\ncount_list\x18\x01 \x03(\x0b\x32\x08.PBCount*g\n\x12MSGID_MODULE_COUNT\x12\x1a\n\x15ID_MODULE_COUNT_BEGIN\x10\x80:\x12\x1b\n\x16ID_MODULE_COUNT_NOTIFY\x10\x81:\x12\x18\n\x13ID_MODULE_COUNT_END\x10\xff;*\x8f\x01\n\x0e\x45\x46reshTimeUnit\x12\x12\n\x0e\x66resh_unit_day\x10\x00\x12\x13\n\x0f\x66resh_unit_hour\x10\x01\x12\x13\n\x0f\x66resh_unit_week\x10\x02\x12\x14\n\x10\x66resh_unit_month\x10\x03\x12\x13\n\x0f\x66resh_unit_year\x10\x04\x12\x14\n\x10\x66resh_unit_never\x10\x05*R\n\rEnCounterType\x12\x10\n\x0c\x43OUNTER_NONE\x10\x00\x12\x15\n\x11\x43OUNTER_PET_CREAM\x10\x01\x12\x18\n\x14\x43OUNTER_KILLCREATURE\x10\x02*\xe5\x03\n\x10PBEnumGuildCount\x12*\n&EGUILD_COUNT_CHAIREMAN_ONLINE_LIVENESS\x10\x01\x12\'\n#EGUILD_COUNT_MEMBER_ONLINE_LIVENESS\x10\x03\x12+\n\'EGUILD_COUNT_MEMBER_ONLINE_LIVENESS_PER\x10\x04\x12\x17\n\x13\x45GUILD_COUNT_DONATE\x10\x05\x12\x1b\n\x17\x45GUILD_COUNT_DONATE_PER\x10\x06\x12\x17\n\x13\x45GUILD_COUNT_DOTASK\x10\x07\x12\x1b\n\x17\x45GUILD_COUNT_DOTASK_PER\x10\x08\x12\x1d\n\x19\x45GUILD_COUNT_OPEN_HOT_POT\x10\t\x12\x1c\n\x18\x45GUILD_COUNT_EAT_HOT_POT\x10\x0b\x12 \n\x1c\x45GUILD_COUNT_EAT_HOT_POT_PER\x10\x0c\x12\x1a\n\x16\x45GUILD_COUNT_OPEN_BOSS\x10\r\x12\x1a\n\x16\x45GUILD_COUNT_KILL_BOSS\x10\x0f\x12#\n\x1f\x45GUILD_COUNT_ENTER_GUILD_BATTLE\x10\x11\x12\'\n#EGUILD_COUNT_ENTER_GUILD_BATTLE_PER\x10\x12\x42\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGID_MODULE_COUNT = _descriptor.EnumDescriptor(
  name='MSGID_MODULE_COUNT',
  full_name='MSGID_MODULE_COUNT',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ID_MODULE_COUNT_BEGIN', index=0, number=7424,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_MODULE_COUNT_NOTIFY', index=1, number=7425,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_MODULE_COUNT_END', index=2, number=7679,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=310,
  serialized_end=413,
)
_sym_db.RegisterEnumDescriptor(_MSGID_MODULE_COUNT)

MSGID_MODULE_COUNT = enum_type_wrapper.EnumTypeWrapper(_MSGID_MODULE_COUNT)
_EFRESHTIMEUNIT = _descriptor.EnumDescriptor(
  name='EFreshTimeUnit',
  full_name='EFreshTimeUnit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='fresh_unit_day', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fresh_unit_hour', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fresh_unit_week', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fresh_unit_month', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fresh_unit_year', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fresh_unit_never', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=416,
  serialized_end=559,
)
_sym_db.RegisterEnumDescriptor(_EFRESHTIMEUNIT)

EFreshTimeUnit = enum_type_wrapper.EnumTypeWrapper(_EFRESHTIMEUNIT)
_ENCOUNTERTYPE = _descriptor.EnumDescriptor(
  name='EnCounterType',
  full_name='EnCounterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COUNTER_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUNTER_PET_CREAM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUNTER_KILLCREATURE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=561,
  serialized_end=643,
)
_sym_db.RegisterEnumDescriptor(_ENCOUNTERTYPE)

EnCounterType = enum_type_wrapper.EnumTypeWrapper(_ENCOUNTERTYPE)
_PBENUMGUILDCOUNT = _descriptor.EnumDescriptor(
  name='PBEnumGuildCount',
  full_name='PBEnumGuildCount',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_CHAIREMAN_ONLINE_LIVENESS', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_MEMBER_ONLINE_LIVENESS', index=1, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_MEMBER_ONLINE_LIVENESS_PER', index=2, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_DONATE', index=3, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_DONATE_PER', index=4, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_DOTASK', index=5, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_DOTASK_PER', index=6, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_OPEN_HOT_POT', index=7, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_EAT_HOT_POT', index=8, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_EAT_HOT_POT_PER', index=9, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_OPEN_BOSS', index=10, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_KILL_BOSS', index=11, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_ENTER_GUILD_BATTLE', index=12, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGUILD_COUNT_ENTER_GUILD_BATTLE_PER', index=13, number=18,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=646,
  serialized_end=1131,
)
_sym_db.RegisterEnumDescriptor(_PBENUMGUILDCOUNT)

PBEnumGuildCount = enum_type_wrapper.EnumTypeWrapper(_PBENUMGUILDCOUNT)
ID_MODULE_COUNT_BEGIN = 7424
ID_MODULE_COUNT_NOTIFY = 7425
ID_MODULE_COUNT_END = 7679
fresh_unit_day = 0
fresh_unit_hour = 1
fresh_unit_week = 2
fresh_unit_month = 3
fresh_unit_year = 4
fresh_unit_never = 5
COUNTER_NONE = 0
COUNTER_PET_CREAM = 1
COUNTER_KILLCREATURE = 2
EGUILD_COUNT_CHAIREMAN_ONLINE_LIVENESS = 1
EGUILD_COUNT_MEMBER_ONLINE_LIVENESS = 3
EGUILD_COUNT_MEMBER_ONLINE_LIVENESS_PER = 4
EGUILD_COUNT_DONATE = 5
EGUILD_COUNT_DONATE_PER = 6
EGUILD_COUNT_DOTASK = 7
EGUILD_COUNT_DOTASK_PER = 8
EGUILD_COUNT_OPEN_HOT_POT = 9
EGUILD_COUNT_EAT_HOT_POT = 11
EGUILD_COUNT_EAT_HOT_POT_PER = 12
EGUILD_COUNT_OPEN_BOSS = 13
EGUILD_COUNT_KILL_BOSS = 15
EGUILD_COUNT_ENTER_GUILD_BATTLE = 17
EGUILD_COUNT_ENTER_GUILD_BATTLE_PER = 18



_PBCOUNTERINFO = _descriptor.Descriptor(
  name='PBCounterInfo',
  full_name='PBCounterInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counter_id', full_name='PBCounterInfo.counter_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times', full_name='PBCounterInfo.times', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_times', full_name='PBCounterInfo.buy_times', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_end=89,
)


_PBCOUNTDATA = _descriptor.Descriptor(
  name='PBCountData',
  full_name='PBCountData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counter_info', full_name='PBCountData.counter_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=91,
  serialized_end=142,
)


_PBCOUNT = _descriptor.Descriptor(
  name='PBCount',
  full_name='PBCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count_type', full_name='PBCount.count_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count_id', full_name='PBCount.count_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_time', full_name='PBCount.max_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times', full_name='PBCount.times', index=3,
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
  serialized_start=144,
  serialized_end=254,
)


_PBS2CROLECOUNTNOFITY = _descriptor.Descriptor(
  name='PBS2CRoleCountNofity',
  full_name='PBS2CRoleCountNofity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count_list', full_name='PBS2CRoleCountNofity.count_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=256,
  serialized_end=308,
)

_PBCOUNTDATA.fields_by_name['counter_info'].message_type = _PBCOUNTERINFO
_PBCOUNT.fields_by_name['count_type'].enum_type = _ENCOUNTERTYPE
_PBS2CROLECOUNTNOFITY.fields_by_name['count_list'].message_type = _PBCOUNT
DESCRIPTOR.message_types_by_name['PBCounterInfo'] = _PBCOUNTERINFO
DESCRIPTOR.message_types_by_name['PBCountData'] = _PBCOUNTDATA
DESCRIPTOR.message_types_by_name['PBCount'] = _PBCOUNT
DESCRIPTOR.message_types_by_name['PBS2CRoleCountNofity'] = _PBS2CROLECOUNTNOFITY
DESCRIPTOR.enum_types_by_name['MSGID_MODULE_COUNT'] = _MSGID_MODULE_COUNT
DESCRIPTOR.enum_types_by_name['EFreshTimeUnit'] = _EFRESHTIMEUNIT
DESCRIPTOR.enum_types_by_name['EnCounterType'] = _ENCOUNTERTYPE
DESCRIPTOR.enum_types_by_name['PBEnumGuildCount'] = _PBENUMGUILDCOUNT

PBCounterInfo = _reflection.GeneratedProtocolMessageType('PBCounterInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBCOUNTERINFO,
  __module__ = 'module_count.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCounterInfo)
  ))
_sym_db.RegisterMessage(PBCounterInfo)

PBCountData = _reflection.GeneratedProtocolMessageType('PBCountData', (_message.Message,), dict(
  DESCRIPTOR = _PBCOUNTDATA,
  __module__ = 'module_count.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCountData)
  ))
_sym_db.RegisterMessage(PBCountData)

PBCount = _reflection.GeneratedProtocolMessageType('PBCount', (_message.Message,), dict(
  DESCRIPTOR = _PBCOUNT,
  __module__ = 'module_count.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCount)
  ))
_sym_db.RegisterMessage(PBCount)

PBS2CRoleCountNofity = _reflection.GeneratedProtocolMessageType('PBS2CRoleCountNofity', (_message.Message,), dict(
  DESCRIPTOR = _PBS2CROLECOUNTNOFITY,
  __module__ = 'module_count.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBS2CRoleCountNofity)
  ))
_sym_db.RegisterMessage(PBS2CRoleCountNofity)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: property_type.hxx

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


import module_define.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='property_type.hxx',
  package='',
  serialized_pb=_b('\n\x11property_type.hxx\x1a\x11module_define.hxx*\xf1\x06\n\x0f\x45OccupationRate\x12\x10\n\x0cMAX_HP_TIZHI\x10\x01\x12\x11\n\rMAX_HP_JINGLI\x10\x02\x12\x1f\n\x1bPHYSICAL_ATTACK_MAX_LILIANG\x10\x03\x12\x1e\n\x1aPHYSICAL_ATTACK_MAX_MINJIE\x10\x04\x12\x1f\n\x1bPHYSICAL_ATTACK_MIN_LILIANG\x10\x05\x12\x1e\n\x1aPHYSICAL_ATTACK_MIN_MINJIE\x10\x06\x12\x1a\n\x16MAGIC_ATTACK_MAX_ZHILI\x10\x07\x12\x1b\n\x17MAGIC_ATTACK_MAX_JINGLI\x10\x08\x12\x1a\n\x16MAGIC_ATTACK_MIN_ZHILI\x10\t\x12\x1b\n\x17MAGIC_ATTACK_MIN_JINGLI\x10\n\x12\x1c\n\x18PHYSICAL_DEFENCE_LILIANG\x10\x0b\x12\x1a\n\x16PHYSICAL_DEFENCE_TIZHI\x10\x0c\x12\x17\n\x13MAGIC_DEFENCE_TIZHI\x10\r\x12\x18\n\x14MAGIC_DEFENCE_JINGLI\x10\x0e\x12\x1d\n\x19PHYSICAL_MINGZHONG_MINJIE\x10\x0f\x12\x1a\n\x16PHYSICAL_SHANBI_MINJIE\x10\x10\x12\x19\n\x15MAGIC_MINGZHONG_ZHILI\x10\x11\x12\x17\n\x13MAGIC_SHANBI_JINGLI\x10\x12\x12\x12\n\x0eGEDANG_LILIANG\x10\x13\x12\x10\n\x0cPODUN_MINJIE\x10\x14\x12\x16\n\x12WULIZHIMING_MINJIE\x10\x15\x12\x16\n\x12\x46\x41SHUZHILING_ZHILI\x10\x16\x12\x12\n\x0eZHILIAO_JINGLI\x10\x17\x12\x1c\n\x18MAGIC_ATTACK_MIN_LILIANG\x10\x18\x12\x1c\n\x18MAGIC_ATTACK_MAX_LILIANG\x10\x19\x12\x15\n\x11WULIZHIMING_ZHILI\x10\x1a\x12\x11\n\rGEDANG_MINJIE\x10\x1b\x12\x1d\n\x19PHYSICAL_MINGZHONG_JINGLI\x10\x1c\x12\x1a\n\x16PHYSICAL_SHANBI_JINGLI\x10\x1d\x12\x1a\n\x16MAGIC_MINGZHONG_JINGLI\x10\x1e\x12\x14\n\x10\x43HUSHI_MINGZHONG\x10\x1f\x12\x11\n\rCHUSHI_SHANBI\x10 \x12\x19\n\x15OCUUPATION_RATE_COUNT\x10!B\x02H\x01')
  ,
  dependencies=[module_define.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EOCCUPATIONRATE = _descriptor.EnumDescriptor(
  name='EOccupationRate',
  full_name='EOccupationRate',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MAX_HP_TIZHI', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_HP_JINGLI', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_ATTACK_MAX_LILIANG', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_ATTACK_MAX_MINJIE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_ATTACK_MIN_LILIANG', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_ATTACK_MIN_MINJIE', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_ATTACK_MAX_ZHILI', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_ATTACK_MAX_JINGLI', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_ATTACK_MIN_ZHILI', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_ATTACK_MIN_JINGLI', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_DEFENCE_LILIANG', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_DEFENCE_TIZHI', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_DEFENCE_TIZHI', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_DEFENCE_JINGLI', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_MINGZHONG_MINJIE', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_SHANBI_MINJIE', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_MINGZHONG_ZHILI', index=16, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_SHANBI_JINGLI', index=17, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEDANG_LILIANG', index=18, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PODUN_MINJIE', index=19, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WULIZHIMING_MINJIE', index=20, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FASHUZHILING_ZHILI', index=21, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZHILIAO_JINGLI', index=22, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_ATTACK_MIN_LILIANG', index=23, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_ATTACK_MAX_LILIANG', index=24, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WULIZHIMING_ZHILI', index=25, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEDANG_MINJIE', index=26, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_MINGZHONG_JINGLI', index=27, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL_SHANBI_JINGLI', index=28, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGIC_MINGZHONG_JINGLI', index=29, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHUSHI_MINGZHONG', index=30, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHUSHI_SHANBI', index=31, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OCUUPATION_RATE_COUNT', index=32, number=33,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=41,
  serialized_end=922,
)
_sym_db.RegisterEnumDescriptor(_EOCCUPATIONRATE)

EOccupationRate = enum_type_wrapper.EnumTypeWrapper(_EOCCUPATIONRATE)
MAX_HP_TIZHI = 1
MAX_HP_JINGLI = 2
PHYSICAL_ATTACK_MAX_LILIANG = 3
PHYSICAL_ATTACK_MAX_MINJIE = 4
PHYSICAL_ATTACK_MIN_LILIANG = 5
PHYSICAL_ATTACK_MIN_MINJIE = 6
MAGIC_ATTACK_MAX_ZHILI = 7
MAGIC_ATTACK_MAX_JINGLI = 8
MAGIC_ATTACK_MIN_ZHILI = 9
MAGIC_ATTACK_MIN_JINGLI = 10
PHYSICAL_DEFENCE_LILIANG = 11
PHYSICAL_DEFENCE_TIZHI = 12
MAGIC_DEFENCE_TIZHI = 13
MAGIC_DEFENCE_JINGLI = 14
PHYSICAL_MINGZHONG_MINJIE = 15
PHYSICAL_SHANBI_MINJIE = 16
MAGIC_MINGZHONG_ZHILI = 17
MAGIC_SHANBI_JINGLI = 18
GEDANG_LILIANG = 19
PODUN_MINJIE = 20
WULIZHIMING_MINJIE = 21
FASHUZHILING_ZHILI = 22
ZHILIAO_JINGLI = 23
MAGIC_ATTACK_MIN_LILIANG = 24
MAGIC_ATTACK_MAX_LILIANG = 25
WULIZHIMING_ZHILI = 26
GEDANG_MINJIE = 27
PHYSICAL_MINGZHONG_JINGLI = 28
PHYSICAL_SHANBI_JINGLI = 29
MAGIC_MINGZHONG_JINGLI = 30
CHUSHI_MINGZHONG = 31
CHUSHI_SHANBI = 32
OCUUPATION_RATE_COUNT = 33


DESCRIPTOR.enum_types_by_name['EOccupationRate'] = _EOCCUPATIONRATE


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

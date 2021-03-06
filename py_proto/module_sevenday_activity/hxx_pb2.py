# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_sevenday_activity.hxx

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
  name='module_sevenday_activity.hxx',
  package='',
  serialized_pb=_b('\n\x1cmodule_sevenday_activity.hxx\x1a\x10module_props.hxx\"Y\n\x0c\x44\x61yAwardList\x12\x11\n\tdraw_flag\x18\x01 \x01(\x08\x12\x11\n\tday_index\x18\x02 \x01(\x05\x12#\n\rday_propslist\x18\x03 \x01(\x0b\x32\x0c.PBPropsList\"b\n\x11SevenDayAwardList\x12$\n\rday_awardlist\x18\x01 \x03(\x0b\x32\r.DayAwardList\x12\x14\n\x0c\x64\x61y_curlogin\x18\x02 \x01(\x05\x12\x11\n\tleft_time\x18\x03 \x01(\x05\"8\n#PBMsgC2SSevenDayAwardDrawReceiveReq\x12\x11\n\tday_index\x18\x01 \x01(\x05\"J\n#PBMsgS2CSevenDayAwardDrawReceiveRes\x12\x11\n\tday_index\x18\x01 \x01(\x05\x12\x10\n\x08ret_code\x18\x02 \x01(\x05\"&\n$PBMsgC2SSevenDayAwardQueryReceiveReq\"Q\n$PBMsgS2CSevenDayAwardQueryReceiveRes\x12)\n\rsevenday_list\x18\x01 \x01(\x0b\x32\x12.SevenDayAwardList*\xa4\x02\n\x1eMSGID_MODULE_SEVENDAY_ACTIVITY\x12>\n9ID_C2S_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_DRAW_REQUEST\x10\x80\x32\x12?\n:ID_S2C_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_DRAW_RESPONSE\x10\x81\x32\x12?\n:ID_C2S_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_QUERY_REQUEST\x10\x82\x32\x12@\n;ID_S2C_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_QUERY_RESPONSE\x10\x83\x32\x42\x02H\x01')
  ,
  dependencies=[module_props.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGID_MODULE_SEVENDAY_ACTIVITY = _descriptor.EnumDescriptor(
  name='MSGID_MODULE_SEVENDAY_ACTIVITY',
  full_name='MSGID_MODULE_SEVENDAY_ACTIVITY',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_DRAW_REQUEST', index=0, number=6400,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_DRAW_RESPONSE', index=1, number=6401,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_QUERY_REQUEST', index=2, number=6402,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_QUERY_RESPONSE', index=3, number=6403,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=499,
  serialized_end=791,
)
_sym_db.RegisterEnumDescriptor(_MSGID_MODULE_SEVENDAY_ACTIVITY)

MSGID_MODULE_SEVENDAY_ACTIVITY = enum_type_wrapper.EnumTypeWrapper(_MSGID_MODULE_SEVENDAY_ACTIVITY)
ID_C2S_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_DRAW_REQUEST = 6400
ID_S2C_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_DRAW_RESPONSE = 6401
ID_C2S_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_QUERY_REQUEST = 6402
ID_S2C_SEVENDAY_ACTIVITY_SEVENDAY_AWARD_LIST_QUERY_RESPONSE = 6403



_DAYAWARDLIST = _descriptor.Descriptor(
  name='DayAwardList',
  full_name='DayAwardList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='draw_flag', full_name='DayAwardList.draw_flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day_index', full_name='DayAwardList.day_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day_propslist', full_name='DayAwardList.day_propslist', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=50,
  serialized_end=139,
)


_SEVENDAYAWARDLIST = _descriptor.Descriptor(
  name='SevenDayAwardList',
  full_name='SevenDayAwardList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='day_awardlist', full_name='SevenDayAwardList.day_awardlist', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day_curlogin', full_name='SevenDayAwardList.day_curlogin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_time', full_name='SevenDayAwardList.left_time', index=2,
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
  serialized_start=141,
  serialized_end=239,
)


_PBMSGC2SSEVENDAYAWARDDRAWRECEIVEREQ = _descriptor.Descriptor(
  name='PBMsgC2SSevenDayAwardDrawReceiveReq',
  full_name='PBMsgC2SSevenDayAwardDrawReceiveReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='day_index', full_name='PBMsgC2SSevenDayAwardDrawReceiveReq.day_index', index=0,
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
  serialized_start=241,
  serialized_end=297,
)


_PBMSGS2CSEVENDAYAWARDDRAWRECEIVERES = _descriptor.Descriptor(
  name='PBMsgS2CSevenDayAwardDrawReceiveRes',
  full_name='PBMsgS2CSevenDayAwardDrawReceiveRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='day_index', full_name='PBMsgS2CSevenDayAwardDrawReceiveRes.day_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgS2CSevenDayAwardDrawReceiveRes.ret_code', index=1,
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
  serialized_start=299,
  serialized_end=373,
)


_PBMSGC2SSEVENDAYAWARDQUERYRECEIVEREQ = _descriptor.Descriptor(
  name='PBMsgC2SSevenDayAwardQueryReceiveReq',
  full_name='PBMsgC2SSevenDayAwardQueryReceiveReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=375,
  serialized_end=413,
)


_PBMSGS2CSEVENDAYAWARDQUERYRECEIVERES = _descriptor.Descriptor(
  name='PBMsgS2CSevenDayAwardQueryReceiveRes',
  full_name='PBMsgS2CSevenDayAwardQueryReceiveRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sevenday_list', full_name='PBMsgS2CSevenDayAwardQueryReceiveRes.sevenday_list', index=0,
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
  serialized_start=415,
  serialized_end=496,
)

_DAYAWARDLIST.fields_by_name['day_propslist'].message_type = module_props.hxx_pb2._PBPROPSLIST
_SEVENDAYAWARDLIST.fields_by_name['day_awardlist'].message_type = _DAYAWARDLIST
_PBMSGS2CSEVENDAYAWARDQUERYRECEIVERES.fields_by_name['sevenday_list'].message_type = _SEVENDAYAWARDLIST
DESCRIPTOR.message_types_by_name['DayAwardList'] = _DAYAWARDLIST
DESCRIPTOR.message_types_by_name['SevenDayAwardList'] = _SEVENDAYAWARDLIST
DESCRIPTOR.message_types_by_name['PBMsgC2SSevenDayAwardDrawReceiveReq'] = _PBMSGC2SSEVENDAYAWARDDRAWRECEIVEREQ
DESCRIPTOR.message_types_by_name['PBMsgS2CSevenDayAwardDrawReceiveRes'] = _PBMSGS2CSEVENDAYAWARDDRAWRECEIVERES
DESCRIPTOR.message_types_by_name['PBMsgC2SSevenDayAwardQueryReceiveReq'] = _PBMSGC2SSEVENDAYAWARDQUERYRECEIVEREQ
DESCRIPTOR.message_types_by_name['PBMsgS2CSevenDayAwardQueryReceiveRes'] = _PBMSGS2CSEVENDAYAWARDQUERYRECEIVERES
DESCRIPTOR.enum_types_by_name['MSGID_MODULE_SEVENDAY_ACTIVITY'] = _MSGID_MODULE_SEVENDAY_ACTIVITY

DayAwardList = _reflection.GeneratedProtocolMessageType('DayAwardList', (_message.Message,), dict(
  DESCRIPTOR = _DAYAWARDLIST,
  __module__ = 'module_sevenday_activity.hxx_pb2'
  # @@protoc_insertion_point(class_scope:DayAwardList)
  ))
_sym_db.RegisterMessage(DayAwardList)

SevenDayAwardList = _reflection.GeneratedProtocolMessageType('SevenDayAwardList', (_message.Message,), dict(
  DESCRIPTOR = _SEVENDAYAWARDLIST,
  __module__ = 'module_sevenday_activity.hxx_pb2'
  # @@protoc_insertion_point(class_scope:SevenDayAwardList)
  ))
_sym_db.RegisterMessage(SevenDayAwardList)

PBMsgC2SSevenDayAwardDrawReceiveReq = _reflection.GeneratedProtocolMessageType('PBMsgC2SSevenDayAwardDrawReceiveReq', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SSEVENDAYAWARDDRAWRECEIVEREQ,
  __module__ = 'module_sevenday_activity.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SSevenDayAwardDrawReceiveReq)
  ))
_sym_db.RegisterMessage(PBMsgC2SSevenDayAwardDrawReceiveReq)

PBMsgS2CSevenDayAwardDrawReceiveRes = _reflection.GeneratedProtocolMessageType('PBMsgS2CSevenDayAwardDrawReceiveRes', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CSEVENDAYAWARDDRAWRECEIVERES,
  __module__ = 'module_sevenday_activity.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CSevenDayAwardDrawReceiveRes)
  ))
_sym_db.RegisterMessage(PBMsgS2CSevenDayAwardDrawReceiveRes)

PBMsgC2SSevenDayAwardQueryReceiveReq = _reflection.GeneratedProtocolMessageType('PBMsgC2SSevenDayAwardQueryReceiveReq', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SSEVENDAYAWARDQUERYRECEIVEREQ,
  __module__ = 'module_sevenday_activity.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SSevenDayAwardQueryReceiveReq)
  ))
_sym_db.RegisterMessage(PBMsgC2SSevenDayAwardQueryReceiveReq)

PBMsgS2CSevenDayAwardQueryReceiveRes = _reflection.GeneratedProtocolMessageType('PBMsgS2CSevenDayAwardQueryReceiveRes', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CSEVENDAYAWARDQUERYRECEIVERES,
  __module__ = 'module_sevenday_activity.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CSevenDayAwardQueryReceiveRes)
  ))
_sym_db.RegisterMessage(PBMsgS2CSevenDayAwardQueryReceiveRes)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

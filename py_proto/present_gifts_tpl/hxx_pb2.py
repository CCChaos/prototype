# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: present_gifts_tpl.hxx

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import module_props.hxx_pb2
import module_scene.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='present_gifts_tpl.hxx',
  package='',
  serialized_pb=_b('\n\x15present_gifts_tpl.hxx\x1a\x10module_props.hxx\x1a\x10module_scene.hxx\"q\n PBMsgS2GCheckUserCpCanAddRequest\x12\x13\n\x0broleid_send\x18\x01 \x01(\x05\x12\x13\n\x0broleid_recv\x18\x02 \x01(\x05\x12\x0f\n\x07gift_id\x18\x03 \x01(\x05\x12\x12\n\ngift_count\x18\x04 \x01(\x05\"\xf0\x01\n!PBMsgG2SCheckUserCpCanAddResponse\x12\x13\n\x0broleid_send\x18\x01 \x01(\x05\x12\x13\n\x0broleid_recv\x18\x02 \x01(\x05\x12\x13\n\x0bnotice_type\x18\x03 \x01(\x05\x12\x16\n\x0esend_notice_id\x18\x04 \x01(\x05\x12\x16\n\x0erecv_notice_id\x18\x05 \x01(\x05\x12\x0f\n\x07user_cp\x18\x06 \x01(\x05\x12\x14\n\x0c\x66riendliness\x18\x07 \x01(\x05\x12\x0f\n\x07gift_id\x18\x08 \x01(\x05\x12\x12\n\ngift_count\x18\t \x01(\x05\x12\x10\n\x08ret_code\x18\n \x01(\x05\"\xd8\x01\n\x1bPBMsgS2GPRESENTGIFTSRequest\x12\x13\n\x0broleid_send\x18\x01 \x01(\x05\x12\x13\n\x0broleid_recv\x18\x02 \x01(\x05\x12\x0f\n\x07user_cp\x18\x03 \x01(\x05\x12\x14\n\x0c\x66riendliness\x18\x04 \x01(\x05\x12\x0f\n\x07gift_id\x18\x05 \x01(\x05\x12\x12\n\ngift_count\x18\x06 \x01(\x05\x12\x13\n\x0bnotice_type\x18\x07 \x01(\x05\x12\x16\n\x0esend_notice_id\x18\x08 \x01(\x05\x12\x16\n\x0erecv_notice_id\x18\t \x01(\x05\"\xe8\x02\n\x1cPBMsgG2SPRESENTGIFTSResponse\x12\x13\n\x0broleid_send\x18\x01 \x01(\x05\x12\x13\n\x0broleid_recv\x18\x02 \x01(\x05\x12\x0f\n\x07gift_id\x18\x03 \x01(\x05\x12\x12\n\ngift_count\x18\x04 \x01(\x05\x12\x13\n\x0bnotice_type\x18\x05 \x01(\x05\x12\x16\n\x0esend_notice_id\x18\x06 \x01(\x05\x12\x16\n\x0erecv_notice_id\x18\x07 \x01(\x05\x12\x14\n\x0crelationship\x18\x08 \x01(\x05\x12\x14\n\x0cthis_user_cp\x18\t \x01(\x05\x12\x19\n\x11this_relationship\x18\n \x01(\x05\x12\x10\n\x08ret_code\x18\x0b \x01(\x05\x12+\n\x10player_main_data\x18\x0c \x01(\x0b\x32\x11.PBPlayerMainData\x12\x16\n\x0erole_name_recv\x18\r \x01(\t\x12\x16\n\x0erole_name_send\x18\x0e \x01(\t\"T\n\x1aPBMsgG2SPRESENTGIFTSNOTIFY\x12\x0f\n\x07role_id\x18\x01 \x01(\x05\x12\x0f\n\x07user_cp\x18\x02 \x01(\x05\x12\x14\n\x0cweek_user_cp\x18\x03 \x01(\x05\"\x9f\x01\n\x0bPBGiftsNode\x12\x0f\n\x07\x64rop_id\x18\x01 \x01(\x05\x12\x0f\n\x07user_cp\x18\x02 \x01(\x05\x12\x14\n\x0c\x66riendliness\x18\x03 \x01(\x05\x12\x13\n\x0bneed_friend\x18\x04 \x01(\x05\x12\x13\n\x0bnotice_type\x18\x05 \x01(\x05\x12\x16\n\x0esend_notice_id\x18\x06 \x01(\x05\x12\x16\n\x0erecv_notice_id\x18\x07 \x01(\x05\x42\x02H\x01')
  ,
  dependencies=[module_props.hxx_pb2.DESCRIPTOR,module_scene.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBMSGS2GCHECKUSERCPCANADDREQUEST = _descriptor.Descriptor(
  name='PBMsgS2GCheckUserCpCanAddRequest',
  full_name='PBMsgS2GCheckUserCpCanAddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleid_send', full_name='PBMsgS2GCheckUserCpCanAddRequest.roleid_send', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roleid_recv', full_name='PBMsgS2GCheckUserCpCanAddRequest.roleid_recv', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='PBMsgS2GCheckUserCpCanAddRequest.gift_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_count', full_name='PBMsgS2GCheckUserCpCanAddRequest.gift_count', index=3,
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
  serialized_start=61,
  serialized_end=174,
)


_PBMSGG2SCHECKUSERCPCANADDRESPONSE = _descriptor.Descriptor(
  name='PBMsgG2SCheckUserCpCanAddResponse',
  full_name='PBMsgG2SCheckUserCpCanAddResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleid_send', full_name='PBMsgG2SCheckUserCpCanAddResponse.roleid_send', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roleid_recv', full_name='PBMsgG2SCheckUserCpCanAddResponse.roleid_recv', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_type', full_name='PBMsgG2SCheckUserCpCanAddResponse.notice_type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_notice_id', full_name='PBMsgG2SCheckUserCpCanAddResponse.send_notice_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recv_notice_id', full_name='PBMsgG2SCheckUserCpCanAddResponse.recv_notice_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_cp', full_name='PBMsgG2SCheckUserCpCanAddResponse.user_cp', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friendliness', full_name='PBMsgG2SCheckUserCpCanAddResponse.friendliness', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='PBMsgG2SCheckUserCpCanAddResponse.gift_id', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_count', full_name='PBMsgG2SCheckUserCpCanAddResponse.gift_count', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgG2SCheckUserCpCanAddResponse.ret_code', index=9,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=177,
  serialized_end=417,
)


_PBMSGS2GPRESENTGIFTSREQUEST = _descriptor.Descriptor(
  name='PBMsgS2GPRESENTGIFTSRequest',
  full_name='PBMsgS2GPRESENTGIFTSRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleid_send', full_name='PBMsgS2GPRESENTGIFTSRequest.roleid_send', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roleid_recv', full_name='PBMsgS2GPRESENTGIFTSRequest.roleid_recv', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_cp', full_name='PBMsgS2GPRESENTGIFTSRequest.user_cp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friendliness', full_name='PBMsgS2GPRESENTGIFTSRequest.friendliness', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='PBMsgS2GPRESENTGIFTSRequest.gift_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_count', full_name='PBMsgS2GPRESENTGIFTSRequest.gift_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_type', full_name='PBMsgS2GPRESENTGIFTSRequest.notice_type', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_notice_id', full_name='PBMsgS2GPRESENTGIFTSRequest.send_notice_id', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recv_notice_id', full_name='PBMsgS2GPRESENTGIFTSRequest.recv_notice_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=420,
  serialized_end=636,
)


_PBMSGG2SPRESENTGIFTSRESPONSE = _descriptor.Descriptor(
  name='PBMsgG2SPRESENTGIFTSResponse',
  full_name='PBMsgG2SPRESENTGIFTSResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleid_send', full_name='PBMsgG2SPRESENTGIFTSResponse.roleid_send', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roleid_recv', full_name='PBMsgG2SPRESENTGIFTSResponse.roleid_recv', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='PBMsgG2SPRESENTGIFTSResponse.gift_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift_count', full_name='PBMsgG2SPRESENTGIFTSResponse.gift_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_type', full_name='PBMsgG2SPRESENTGIFTSResponse.notice_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_notice_id', full_name='PBMsgG2SPRESENTGIFTSResponse.send_notice_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recv_notice_id', full_name='PBMsgG2SPRESENTGIFTSResponse.recv_notice_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship', full_name='PBMsgG2SPRESENTGIFTSResponse.relationship', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='this_user_cp', full_name='PBMsgG2SPRESENTGIFTSResponse.this_user_cp', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='this_relationship', full_name='PBMsgG2SPRESENTGIFTSResponse.this_relationship', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgG2SPRESENTGIFTSResponse.ret_code', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_main_data', full_name='PBMsgG2SPRESENTGIFTSResponse.player_main_data', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_name_recv', full_name='PBMsgG2SPRESENTGIFTSResponse.role_name_recv', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_name_send', full_name='PBMsgG2SPRESENTGIFTSResponse.role_name_send', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_start=639,
  serialized_end=999,
)


_PBMSGG2SPRESENTGIFTSNOTIFY = _descriptor.Descriptor(
  name='PBMsgG2SPRESENTGIFTSNOTIFY',
  full_name='PBMsgG2SPRESENTGIFTSNOTIFY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgG2SPRESENTGIFTSNOTIFY.role_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_cp', full_name='PBMsgG2SPRESENTGIFTSNOTIFY.user_cp', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='week_user_cp', full_name='PBMsgG2SPRESENTGIFTSNOTIFY.week_user_cp', index=2,
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
  serialized_start=1001,
  serialized_end=1085,
)


_PBGIFTSNODE = _descriptor.Descriptor(
  name='PBGiftsNode',
  full_name='PBGiftsNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='drop_id', full_name='PBGiftsNode.drop_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_cp', full_name='PBGiftsNode.user_cp', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friendliness', full_name='PBGiftsNode.friendliness', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='need_friend', full_name='PBGiftsNode.need_friend', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_type', full_name='PBGiftsNode.notice_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_notice_id', full_name='PBGiftsNode.send_notice_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recv_notice_id', full_name='PBGiftsNode.recv_notice_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=1088,
  serialized_end=1247,
)

_PBMSGG2SPRESENTGIFTSRESPONSE.fields_by_name['player_main_data'].message_type = module_scene.hxx_pb2._PBPLAYERMAINDATA
DESCRIPTOR.message_types_by_name['PBMsgS2GCheckUserCpCanAddRequest'] = _PBMSGS2GCHECKUSERCPCANADDREQUEST
DESCRIPTOR.message_types_by_name['PBMsgG2SCheckUserCpCanAddResponse'] = _PBMSGG2SCHECKUSERCPCANADDRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgS2GPRESENTGIFTSRequest'] = _PBMSGS2GPRESENTGIFTSREQUEST
DESCRIPTOR.message_types_by_name['PBMsgG2SPRESENTGIFTSResponse'] = _PBMSGG2SPRESENTGIFTSRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgG2SPRESENTGIFTSNOTIFY'] = _PBMSGG2SPRESENTGIFTSNOTIFY
DESCRIPTOR.message_types_by_name['PBGiftsNode'] = _PBGIFTSNODE

PBMsgS2GCheckUserCpCanAddRequest = _reflection.GeneratedProtocolMessageType('PBMsgS2GCheckUserCpCanAddRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2GCHECKUSERCPCANADDREQUEST,
  __module__ = 'present_gifts_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2GCheckUserCpCanAddRequest)
  ))
_sym_db.RegisterMessage(PBMsgS2GCheckUserCpCanAddRequest)

PBMsgG2SCheckUserCpCanAddResponse = _reflection.GeneratedProtocolMessageType('PBMsgG2SCheckUserCpCanAddResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2SCHECKUSERCPCANADDRESPONSE,
  __module__ = 'present_gifts_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2SCheckUserCpCanAddResponse)
  ))
_sym_db.RegisterMessage(PBMsgG2SCheckUserCpCanAddResponse)

PBMsgS2GPRESENTGIFTSRequest = _reflection.GeneratedProtocolMessageType('PBMsgS2GPRESENTGIFTSRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2GPRESENTGIFTSREQUEST,
  __module__ = 'present_gifts_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2GPRESENTGIFTSRequest)
  ))
_sym_db.RegisterMessage(PBMsgS2GPRESENTGIFTSRequest)

PBMsgG2SPRESENTGIFTSResponse = _reflection.GeneratedProtocolMessageType('PBMsgG2SPRESENTGIFTSResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2SPRESENTGIFTSRESPONSE,
  __module__ = 'present_gifts_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2SPRESENTGIFTSResponse)
  ))
_sym_db.RegisterMessage(PBMsgG2SPRESENTGIFTSResponse)

PBMsgG2SPRESENTGIFTSNOTIFY = _reflection.GeneratedProtocolMessageType('PBMsgG2SPRESENTGIFTSNOTIFY', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2SPRESENTGIFTSNOTIFY,
  __module__ = 'present_gifts_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2SPRESENTGIFTSNOTIFY)
  ))
_sym_db.RegisterMessage(PBMsgG2SPRESENTGIFTSNOTIFY)

PBGiftsNode = _reflection.GeneratedProtocolMessageType('PBGiftsNode', (_message.Message,), dict(
  DESCRIPTOR = _PBGIFTSNODE,
  __module__ = 'present_gifts_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBGiftsNode)
  ))
_sym_db.RegisterMessage(PBGiftsNode)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
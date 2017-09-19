# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat_config.hxx

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import module_chat.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat_config.hxx',
  package='',
  serialized_pb=_b('\n\x0f\x63hat_config.hxx\x1a\x0fmodule_chat.hxx\"4\n\rPBChatConsume\x12\x12\n\nconsume_id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63onsume\x18\x02 \x01(\t\"\xb1\x01\n\x0fPBChannelConfig\x12\'\n\x0c\x63hannel_type\x18\x01 \x01(\x0e\x32\x11.EChatChannelType\x12\x1b\n\x13limit_time_interval\x18\x02 \x01(\x05\x12\x1c\n\x14limit_content_length\x18\x03 \x01(\x05\x12\x13\n\x0blimit_level\x18\x04 \x01(\x05\x12%\n\rlimit_consume\x18\x05 \x03(\x0b\x32\x0e.PBChatConsume\"w\n\x0ePBSystemNotice\x12\x13\n\x0b\x64rop_notice\x18\x01 \x01(\x05\x12\x18\n\x10team_join_notice\x18\x02 \x01(\x05\x12\x19\n\x11team_leave_notice\x18\x03 \x01(\x05\x12\x1b\n\x13team_captain_notice\x18\x04 \x01(\x05\"^\n\x0cPBChatConfig\x12&\n\x0c\x63hannel_list\x18\x01 \x03(\x0b\x32\x10.PBChannelConfig\x12&\n\rsystem_notice\x18\x02 \x01(\x0b\x32\x0f.PBSystemNoticeB\x02H\x01')
  ,
  dependencies=[module_chat.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBCHATCONSUME = _descriptor.Descriptor(
  name='PBChatConsume',
  full_name='PBChatConsume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consume_id', full_name='PBChatConsume.consume_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume', full_name='PBChatConsume.consume', index=1,
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
  serialized_start=36,
  serialized_end=88,
)


_PBCHANNELCONFIG = _descriptor.Descriptor(
  name='PBChannelConfig',
  full_name='PBChannelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_type', full_name='PBChannelConfig.channel_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit_time_interval', full_name='PBChannelConfig.limit_time_interval', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit_content_length', full_name='PBChannelConfig.limit_content_length', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit_level', full_name='PBChannelConfig.limit_level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit_consume', full_name='PBChannelConfig.limit_consume', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_end=268,
)


_PBSYSTEMNOTICE = _descriptor.Descriptor(
  name='PBSystemNotice',
  full_name='PBSystemNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='drop_notice', full_name='PBSystemNotice.drop_notice', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team_join_notice', full_name='PBSystemNotice.team_join_notice', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team_leave_notice', full_name='PBSystemNotice.team_leave_notice', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team_captain_notice', full_name='PBSystemNotice.team_captain_notice', index=3,
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
  serialized_start=270,
  serialized_end=389,
)


_PBCHATCONFIG = _descriptor.Descriptor(
  name='PBChatConfig',
  full_name='PBChatConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_list', full_name='PBChatConfig.channel_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_notice', full_name='PBChatConfig.system_notice', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=391,
  serialized_end=485,
)

_PBCHANNELCONFIG.fields_by_name['channel_type'].enum_type = module_chat.hxx_pb2._ECHATCHANNELTYPE
_PBCHANNELCONFIG.fields_by_name['limit_consume'].message_type = _PBCHATCONSUME
_PBCHATCONFIG.fields_by_name['channel_list'].message_type = _PBCHANNELCONFIG
_PBCHATCONFIG.fields_by_name['system_notice'].message_type = _PBSYSTEMNOTICE
DESCRIPTOR.message_types_by_name['PBChatConsume'] = _PBCHATCONSUME
DESCRIPTOR.message_types_by_name['PBChannelConfig'] = _PBCHANNELCONFIG
DESCRIPTOR.message_types_by_name['PBSystemNotice'] = _PBSYSTEMNOTICE
DESCRIPTOR.message_types_by_name['PBChatConfig'] = _PBCHATCONFIG

PBChatConsume = _reflection.GeneratedProtocolMessageType('PBChatConsume', (_message.Message,), dict(
  DESCRIPTOR = _PBCHATCONSUME,
  __module__ = 'chat_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBChatConsume)
  ))
_sym_db.RegisterMessage(PBChatConsume)

PBChannelConfig = _reflection.GeneratedProtocolMessageType('PBChannelConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBCHANNELCONFIG,
  __module__ = 'chat_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBChannelConfig)
  ))
_sym_db.RegisterMessage(PBChannelConfig)

PBSystemNotice = _reflection.GeneratedProtocolMessageType('PBSystemNotice', (_message.Message,), dict(
  DESCRIPTOR = _PBSYSTEMNOTICE,
  __module__ = 'chat_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBSystemNotice)
  ))
_sym_db.RegisterMessage(PBSystemNotice)

PBChatConfig = _reflection.GeneratedProtocolMessageType('PBChatConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBCHATCONFIG,
  __module__ = 'chat_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBChatConfig)
  ))
_sym_db.RegisterMessage(PBChatConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
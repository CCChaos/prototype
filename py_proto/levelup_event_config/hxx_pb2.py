# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: levelup_event_config.hxx

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import module_define.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='levelup_event_config.hxx',
  package='',
  serialized_pb=_b('\n\x18levelup_event_config.hxx\x1a\x11module_define.hxx\"d\n\x0bPBRoleEvent\x12%\n\nevent_type\x18\x01 \x01(\x0e\x32\x11.EPlayerEventType\x12\x0e\n\x06param1\x18\x02 \x01(\x05\x12\x0e\n\x06param2\x18\x03 \x01(\x05\x12\x0e\n\x06params\x18\x04 \x01(\t\"<\n\x0ePBLevelUpEvent\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x1b\n\x05\x65vent\x18\x02 \x03(\x0b\x32\x0c.PBRoleEvent\"<\n\x14PBLevelupEventConfig\x12$\n\x0blevel_event\x18\x01 \x03(\x0b\x32\x0f.PBLevelUpEventB\x02H\x01')
  ,
  dependencies=[module_define.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBROLEEVENT = _descriptor.Descriptor(
  name='PBRoleEvent',
  full_name='PBRoleEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_type', full_name='PBRoleEvent.event_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param1', full_name='PBRoleEvent.param1', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param2', full_name='PBRoleEvent.param2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='PBRoleEvent.params', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=47,
  serialized_end=147,
)


_PBLEVELUPEVENT = _descriptor.Descriptor(
  name='PBLevelUpEvent',
  full_name='PBLevelUpEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='PBLevelUpEvent.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='PBLevelUpEvent.event', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=149,
  serialized_end=209,
)


_PBLEVELUPEVENTCONFIG = _descriptor.Descriptor(
  name='PBLevelupEventConfig',
  full_name='PBLevelupEventConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level_event', full_name='PBLevelupEventConfig.level_event', index=0,
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
  serialized_start=211,
  serialized_end=271,
)

_PBROLEEVENT.fields_by_name['event_type'].enum_type = module_define.hxx_pb2._EPLAYEREVENTTYPE
_PBLEVELUPEVENT.fields_by_name['event'].message_type = _PBROLEEVENT
_PBLEVELUPEVENTCONFIG.fields_by_name['level_event'].message_type = _PBLEVELUPEVENT
DESCRIPTOR.message_types_by_name['PBRoleEvent'] = _PBROLEEVENT
DESCRIPTOR.message_types_by_name['PBLevelUpEvent'] = _PBLEVELUPEVENT
DESCRIPTOR.message_types_by_name['PBLevelupEventConfig'] = _PBLEVELUPEVENTCONFIG

PBRoleEvent = _reflection.GeneratedProtocolMessageType('PBRoleEvent', (_message.Message,), dict(
  DESCRIPTOR = _PBROLEEVENT,
  __module__ = 'levelup_event_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBRoleEvent)
  ))
_sym_db.RegisterMessage(PBRoleEvent)

PBLevelUpEvent = _reflection.GeneratedProtocolMessageType('PBLevelUpEvent', (_message.Message,), dict(
  DESCRIPTOR = _PBLEVELUPEVENT,
  __module__ = 'levelup_event_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBLevelUpEvent)
  ))
_sym_db.RegisterMessage(PBLevelUpEvent)

PBLevelupEventConfig = _reflection.GeneratedProtocolMessageType('PBLevelupEventConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBLEVELUPEVENTCONFIG,
  __module__ = 'levelup_event_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBLevelupEventConfig)
  ))
_sym_db.RegisterMessage(PBLevelupEventConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

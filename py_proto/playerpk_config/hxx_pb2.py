# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playerpk_config.hxx

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='playerpk_config.hxx',
  package='',
  serialized_pb=_b('\n\x13playerpk_config.hxx\"\x84\x01\n\x10PBPlayerPkConfig\x12\x0f\n\x07open_lv\x18\x01 \x01(\x05\x12\x0f\n\x07pk_time\x18\x02 \x01(\x05\x12\x17\n\x0frequest_timeout\x18\x03 \x01(\x05\x12\x10\n\x08\x64istance\x18\x04 \x01(\x05\x12\x0e\n\x06npc_id\x18\x05 \x01(\x05\x12\x13\n\x0bstart_fight\x18\x06 \x01(\x05\x42\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBPLAYERPKCONFIG = _descriptor.Descriptor(
  name='PBPlayerPkConfig',
  full_name='PBPlayerPkConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='open_lv', full_name='PBPlayerPkConfig.open_lv', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pk_time', full_name='PBPlayerPkConfig.pk_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_timeout', full_name='PBPlayerPkConfig.request_timeout', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='PBPlayerPkConfig.distance', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='npc_id', full_name='PBPlayerPkConfig.npc_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_fight', full_name='PBPlayerPkConfig.start_fight', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=24,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['PBPlayerPkConfig'] = _PBPLAYERPKCONFIG

PBPlayerPkConfig = _reflection.GeneratedProtocolMessageType('PBPlayerPkConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBPLAYERPKCONFIG,
  __module__ = 'playerpk_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBPlayerPkConfig)
  ))
_sym_db.RegisterMessage(PBPlayerPkConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
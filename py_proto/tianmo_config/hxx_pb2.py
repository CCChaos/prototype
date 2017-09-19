# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tianmo_config.hxx

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
  name='tianmo_config.hxx',
  package='',
  serialized_pb=_b('\n\x11tianmo_config.hxx\"e\n\x16PBTianmoEntranceConfig\x12\x13\n\x0b\x63reature_id\x18\x01 \x01(\x05\x12\x10\n\x08scene_id\x18\x02 \x01(\x05\x12\x11\n\tmin_level\x18\x03 \x01(\x05\x12\x11\n\tmax_level\x18\x04 \x01(\x05\"m\n\x0ePBTianmoConfig\x12\x1e\n\x16min_challege_team_size\x18\x01 \x01(\x05\x12)\n\x08\x65ntrance\x18\x02 \x03(\x0b\x32\x17.PBTianmoEntranceConfig\x12\x10\n\x08robot_ai\x18\x03 \x01(\tB\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBTIANMOENTRANCECONFIG = _descriptor.Descriptor(
  name='PBTianmoEntranceConfig',
  full_name='PBTianmoEntranceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creature_id', full_name='PBTianmoEntranceConfig.creature_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='PBTianmoEntranceConfig.scene_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_level', full_name='PBTianmoEntranceConfig.min_level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_level', full_name='PBTianmoEntranceConfig.max_level', index=3,
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
  serialized_start=21,
  serialized_end=122,
)


_PBTIANMOCONFIG = _descriptor.Descriptor(
  name='PBTianmoConfig',
  full_name='PBTianmoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_challege_team_size', full_name='PBTianmoConfig.min_challege_team_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entrance', full_name='PBTianmoConfig.entrance', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='robot_ai', full_name='PBTianmoConfig.robot_ai', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=124,
  serialized_end=233,
)

_PBTIANMOCONFIG.fields_by_name['entrance'].message_type = _PBTIANMOENTRANCECONFIG
DESCRIPTOR.message_types_by_name['PBTianmoEntranceConfig'] = _PBTIANMOENTRANCECONFIG
DESCRIPTOR.message_types_by_name['PBTianmoConfig'] = _PBTIANMOCONFIG

PBTianmoEntranceConfig = _reflection.GeneratedProtocolMessageType('PBTianmoEntranceConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBTIANMOENTRANCECONFIG,
  __module__ = 'tianmo_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBTianmoEntranceConfig)
  ))
_sym_db.RegisterMessage(PBTianmoEntranceConfig)

PBTianmoConfig = _reflection.GeneratedProtocolMessageType('PBTianmoConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBTIANMOCONFIG,
  __module__ = 'tianmo_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBTianmoConfig)
  ))
_sym_db.RegisterMessage(PBTianmoConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
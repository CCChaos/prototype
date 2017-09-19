# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mount_tpl.hxx

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
import module_mount.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mount_tpl.hxx',
  package='',
  serialized_pb=_b('\n\rmount_tpl.hxx\x1a\x11module_define.hxx\x1a\x10module_mount.hxx\"\xaf\x01\n\nPBMountTpl\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x62uff_id\x18\x02 \x01(\x05\x12 \n\x0bmount_class\x18\x03 \x01(\x0e\x32\x0b.EItemColor\x12*\n\x10mount_layer_type\x18\x04 \x01(\x0e\x32\x10.EMountLayerType\x12\x0f\n\x07ride_cd\x18\x05 \x01(\x05\x12\x12\n\nbase_power\x18\x06 \x01(\x05\x12\x11\n\tnotice_id\x18\x07 \x01(\x05\"R\n\x17PBMountIllustrationInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x0bunlock_type\x18\x02 \x01(\x05:\x01\x31\x12\x13\n\x0bunlock_item\x18\x03 \x01(\t\"8\n\rPBMountConfig\x12\'\n\x05mount\x18\x01 \x03(\x0b\x32\x18.PBMountIllustrationInfoB\x02H\x01')
  ,
  dependencies=[module_define.hxx_pb2.DESCRIPTOR,module_mount.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBMOUNTTPL = _descriptor.Descriptor(
  name='PBMountTpl',
  full_name='PBMountTpl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PBMountTpl.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buff_id', full_name='PBMountTpl.buff_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_class', full_name='PBMountTpl.mount_class', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_layer_type', full_name='PBMountTpl.mount_layer_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ride_cd', full_name='PBMountTpl.ride_cd', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_power', full_name='PBMountTpl.base_power', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_id', full_name='PBMountTpl.notice_id', index=6,
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
  serialized_start=55,
  serialized_end=230,
)


_PBMOUNTILLUSTRATIONINFO = _descriptor.Descriptor(
  name='PBMountIllustrationInfo',
  full_name='PBMountIllustrationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PBMountIllustrationInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unlock_type', full_name='PBMountIllustrationInfo.unlock_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unlock_item', full_name='PBMountIllustrationInfo.unlock_item', index=2,
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
  serialized_start=232,
  serialized_end=314,
)


_PBMOUNTCONFIG = _descriptor.Descriptor(
  name='PBMountConfig',
  full_name='PBMountConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount', full_name='PBMountConfig.mount', index=0,
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
  serialized_start=316,
  serialized_end=372,
)

_PBMOUNTTPL.fields_by_name['mount_class'].enum_type = module_define.hxx_pb2._EITEMCOLOR
_PBMOUNTTPL.fields_by_name['mount_layer_type'].enum_type = module_mount.hxx_pb2._EMOUNTLAYERTYPE
_PBMOUNTCONFIG.fields_by_name['mount'].message_type = _PBMOUNTILLUSTRATIONINFO
DESCRIPTOR.message_types_by_name['PBMountTpl'] = _PBMOUNTTPL
DESCRIPTOR.message_types_by_name['PBMountIllustrationInfo'] = _PBMOUNTILLUSTRATIONINFO
DESCRIPTOR.message_types_by_name['PBMountConfig'] = _PBMOUNTCONFIG

PBMountTpl = _reflection.GeneratedProtocolMessageType('PBMountTpl', (_message.Message,), dict(
  DESCRIPTOR = _PBMOUNTTPL,
  __module__ = 'mount_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMountTpl)
  ))
_sym_db.RegisterMessage(PBMountTpl)

PBMountIllustrationInfo = _reflection.GeneratedProtocolMessageType('PBMountIllustrationInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBMOUNTILLUSTRATIONINFO,
  __module__ = 'mount_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMountIllustrationInfo)
  ))
_sym_db.RegisterMessage(PBMountIllustrationInfo)

PBMountConfig = _reflection.GeneratedProtocolMessageType('PBMountConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBMOUNTCONFIG,
  __module__ = 'mount_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMountConfig)
  ))
_sym_db.RegisterMessage(PBMountConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

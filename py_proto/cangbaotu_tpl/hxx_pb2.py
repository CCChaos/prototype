# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cangbaotu_tpl.hxx

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
  name='cangbaotu_tpl.hxx',
  package='',
  serialized_pb=_b('\n\x11\x63\x61ngbaotu_tpl.hxx\"5\n\x14PBCangbaotuEventDrop\x12\x0e\n\x06reward\x18\x01 \x01(\t\x12\r\n\x05ratio\x18\x02 \x01(\x05\"?\n\x1cPBCangbaotuEventEnterDungeon\x12\x10\n\x08scene_id\x18\x01 \x01(\x05\x12\r\n\x05ratio\x18\x02 \x01(\x05\"W\n\x19PBCangbaotuEventFlushBoss\x12\x0f\n\x07\x62oss_id\x18\x01 \x01(\x05\x12\x0c\n\x04\x61ngl\x18\x02 \x01(\x02\x12\r\n\x05ratio\x18\x03 \x01(\x05\x12\x0c\n\x04life\x18\x04 \x01(\x05\"\x88\x01\n\x18PBCangbaotuEventFlushNPC\x12\x0e\n\x06npc_id\x18\x01 \x01(\x05\x12\x10\n\x08scene_id\x18\x02 \x01(\x05\x12\t\n\x01x\x18\x03 \x01(\x02\x12\t\n\x01y\x18\x04 \x01(\x02\x12\t\n\x01z\x18\x05 \x01(\x02\x12\x0c\n\x04\x61ngl\x18\x06 \x01(\x02\x12\r\n\x05ratio\x18\x07 \x01(\x05\x12\x0c\n\x04life\x18\x08 \x01(\x05\"\x83\x02\n\x0fPBCangbaotuProp\x12\x0f\n\x07prop_id\x18\x01 \x01(\t\x12\x11\n\tdun_limit\x18\x02 \x01(\x05\x12\x12\n\nboss_limit\x18\x03 \x01(\x05\x12\x11\n\tnpc_limit\x18\x04 \x01(\x05\x12#\n\x04\x64rop\x18\x05 \x03(\x0b\x32\x15.PBCangbaotuEventDrop\x12.\n\x07\x64ungeon\x18\x06 \x03(\x0b\x32\x1d.PBCangbaotuEventEnterDungeon\x12(\n\x04\x62oss\x18\x07 \x03(\x0b\x32\x1a.PBCangbaotuEventFlushBoss\x12&\n\x03npc\x18\x08 \x03(\x0b\x32\x19.PBCangbaotuEventFlushNPC\"\xa0\x01\n\x11PBCangbaotuConfig\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\x05\x12\x1e\n\x04prop\x18\x02 \x03(\x0b\x32\x10.PBCangbaotuProp\x12\x13\n\x0bnotice_boss\x18\x03 \x01(\x05\x12\x12\n\nnotice_npc\x18\x04 \x01(\x05\x12\x13\n\x0bnotice_drop\x18\x05 \x01(\x05\x12\x18\n\x10notice_boss_kill\x18\x06 \x01(\x05\x42\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBCANGBAOTUEVENTDROP = _descriptor.Descriptor(
  name='PBCangbaotuEventDrop',
  full_name='PBCangbaotuEventDrop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reward', full_name='PBCangbaotuEventDrop.reward', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ratio', full_name='PBCangbaotuEventDrop.ratio', index=1,
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
  serialized_start=21,
  serialized_end=74,
)


_PBCANGBAOTUEVENTENTERDUNGEON = _descriptor.Descriptor(
  name='PBCangbaotuEventEnterDungeon',
  full_name='PBCangbaotuEventEnterDungeon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='PBCangbaotuEventEnterDungeon.scene_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ratio', full_name='PBCangbaotuEventEnterDungeon.ratio', index=1,
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
  serialized_start=76,
  serialized_end=139,
)


_PBCANGBAOTUEVENTFLUSHBOSS = _descriptor.Descriptor(
  name='PBCangbaotuEventFlushBoss',
  full_name='PBCangbaotuEventFlushBoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boss_id', full_name='PBCangbaotuEventFlushBoss.boss_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angl', full_name='PBCangbaotuEventFlushBoss.angl', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ratio', full_name='PBCangbaotuEventFlushBoss.ratio', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='life', full_name='PBCangbaotuEventFlushBoss.life', index=3,
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
  serialized_start=141,
  serialized_end=228,
)


_PBCANGBAOTUEVENTFLUSHNPC = _descriptor.Descriptor(
  name='PBCangbaotuEventFlushNPC',
  full_name='PBCangbaotuEventFlushNPC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='npc_id', full_name='PBCangbaotuEventFlushNPC.npc_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='PBCangbaotuEventFlushNPC.scene_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='PBCangbaotuEventFlushNPC.x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='PBCangbaotuEventFlushNPC.y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='PBCangbaotuEventFlushNPC.z', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angl', full_name='PBCangbaotuEventFlushNPC.angl', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ratio', full_name='PBCangbaotuEventFlushNPC.ratio', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='life', full_name='PBCangbaotuEventFlushNPC.life', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=231,
  serialized_end=367,
)


_PBCANGBAOTUPROP = _descriptor.Descriptor(
  name='PBCangbaotuProp',
  full_name='PBCangbaotuProp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prop_id', full_name='PBCangbaotuProp.prop_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dun_limit', full_name='PBCangbaotuProp.dun_limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boss_limit', full_name='PBCangbaotuProp.boss_limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='npc_limit', full_name='PBCangbaotuProp.npc_limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='PBCangbaotuProp.drop', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dungeon', full_name='PBCangbaotuProp.dungeon', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boss', full_name='PBCangbaotuProp.boss', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='npc', full_name='PBCangbaotuProp.npc', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=370,
  serialized_end=629,
)


_PBCANGBAOTUCONFIG = _descriptor.Descriptor(
  name='PBCangbaotuConfig',
  full_name='PBCangbaotuConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_id', full_name='PBCangbaotuConfig.activity_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prop', full_name='PBCangbaotuConfig.prop', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_boss', full_name='PBCangbaotuConfig.notice_boss', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_npc', full_name='PBCangbaotuConfig.notice_npc', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_drop', full_name='PBCangbaotuConfig.notice_drop', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_boss_kill', full_name='PBCangbaotuConfig.notice_boss_kill', index=5,
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
  serialized_start=632,
  serialized_end=792,
)

_PBCANGBAOTUPROP.fields_by_name['drop'].message_type = _PBCANGBAOTUEVENTDROP
_PBCANGBAOTUPROP.fields_by_name['dungeon'].message_type = _PBCANGBAOTUEVENTENTERDUNGEON
_PBCANGBAOTUPROP.fields_by_name['boss'].message_type = _PBCANGBAOTUEVENTFLUSHBOSS
_PBCANGBAOTUPROP.fields_by_name['npc'].message_type = _PBCANGBAOTUEVENTFLUSHNPC
_PBCANGBAOTUCONFIG.fields_by_name['prop'].message_type = _PBCANGBAOTUPROP
DESCRIPTOR.message_types_by_name['PBCangbaotuEventDrop'] = _PBCANGBAOTUEVENTDROP
DESCRIPTOR.message_types_by_name['PBCangbaotuEventEnterDungeon'] = _PBCANGBAOTUEVENTENTERDUNGEON
DESCRIPTOR.message_types_by_name['PBCangbaotuEventFlushBoss'] = _PBCANGBAOTUEVENTFLUSHBOSS
DESCRIPTOR.message_types_by_name['PBCangbaotuEventFlushNPC'] = _PBCANGBAOTUEVENTFLUSHNPC
DESCRIPTOR.message_types_by_name['PBCangbaotuProp'] = _PBCANGBAOTUPROP
DESCRIPTOR.message_types_by_name['PBCangbaotuConfig'] = _PBCANGBAOTUCONFIG

PBCangbaotuEventDrop = _reflection.GeneratedProtocolMessageType('PBCangbaotuEventDrop', (_message.Message,), dict(
  DESCRIPTOR = _PBCANGBAOTUEVENTDROP,
  __module__ = 'cangbaotu_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCangbaotuEventDrop)
  ))
_sym_db.RegisterMessage(PBCangbaotuEventDrop)

PBCangbaotuEventEnterDungeon = _reflection.GeneratedProtocolMessageType('PBCangbaotuEventEnterDungeon', (_message.Message,), dict(
  DESCRIPTOR = _PBCANGBAOTUEVENTENTERDUNGEON,
  __module__ = 'cangbaotu_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCangbaotuEventEnterDungeon)
  ))
_sym_db.RegisterMessage(PBCangbaotuEventEnterDungeon)

PBCangbaotuEventFlushBoss = _reflection.GeneratedProtocolMessageType('PBCangbaotuEventFlushBoss', (_message.Message,), dict(
  DESCRIPTOR = _PBCANGBAOTUEVENTFLUSHBOSS,
  __module__ = 'cangbaotu_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCangbaotuEventFlushBoss)
  ))
_sym_db.RegisterMessage(PBCangbaotuEventFlushBoss)

PBCangbaotuEventFlushNPC = _reflection.GeneratedProtocolMessageType('PBCangbaotuEventFlushNPC', (_message.Message,), dict(
  DESCRIPTOR = _PBCANGBAOTUEVENTFLUSHNPC,
  __module__ = 'cangbaotu_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCangbaotuEventFlushNPC)
  ))
_sym_db.RegisterMessage(PBCangbaotuEventFlushNPC)

PBCangbaotuProp = _reflection.GeneratedProtocolMessageType('PBCangbaotuProp', (_message.Message,), dict(
  DESCRIPTOR = _PBCANGBAOTUPROP,
  __module__ = 'cangbaotu_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCangbaotuProp)
  ))
_sym_db.RegisterMessage(PBCangbaotuProp)

PBCangbaotuConfig = _reflection.GeneratedProtocolMessageType('PBCangbaotuConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBCANGBAOTUCONFIG,
  __module__ = 'cangbaotu_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCangbaotuConfig)
  ))
_sym_db.RegisterMessage(PBCangbaotuConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
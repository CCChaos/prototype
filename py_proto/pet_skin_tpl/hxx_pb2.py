# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pet_skin_tpl.hxx

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
  name='pet_skin_tpl.hxx',
  package='',
  serialized_pb=_b('\n\x10pet_skin_tpl.hxx\x1a\x11module_define.hxx\"e\n\x11PBTplPetInitSkill\x12\"\n\nskill_type\x18\x01 \x01(\x0e\x32\x0e.EPetSkillType\x12\x15\n\rinit_skill_id\x18\x02 \x01(\x05\x12\x15\n\rinit_skill_lv\x18\x03 \x01(\x05\"\xb6\x01\n\x0cPBTplPetSkin\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nexpiration\x18\x02 \x01(\t\x12\x13\n\x0bunlock_cond\x18\x03 \x01(\t\x12%\n\x0bproperty_up\x18\x04 \x03(\x0b\x32\x10.PBBasicProperty\x12\x0f\n\x07\x63onsume\x18\x05 \x01(\t\x12&\n\ninit_skill\x18\x06 \x03(\x0b\x32\x12.PBTplPetInitSkill\x12\x11\n\tnotice_id\x18\x07 \x01(\x05\x42\x02H\x01')
  ,
  dependencies=[module_define.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBTPLPETINITSKILL = _descriptor.Descriptor(
  name='PBTplPetInitSkill',
  full_name='PBTplPetInitSkill',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skill_type', full_name='PBTplPetInitSkill.skill_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_skill_id', full_name='PBTplPetInitSkill.init_skill_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_skill_lv', full_name='PBTplPetInitSkill.init_skill_lv', index=2,
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
  serialized_start=39,
  serialized_end=140,
)


_PBTPLPETSKIN = _descriptor.Descriptor(
  name='PBTplPetSkin',
  full_name='PBTplPetSkin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PBTplPetSkin.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='PBTplPetSkin.expiration', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unlock_cond', full_name='PBTplPetSkin.unlock_cond', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property_up', full_name='PBTplPetSkin.property_up', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume', full_name='PBTplPetSkin.consume', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_skill', full_name='PBTplPetSkin.init_skill', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notice_id', full_name='PBTplPetSkin.notice_id', index=6,
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
  serialized_start=143,
  serialized_end=325,
)

_PBTPLPETINITSKILL.fields_by_name['skill_type'].enum_type = module_define.hxx_pb2._EPETSKILLTYPE
_PBTPLPETSKIN.fields_by_name['property_up'].message_type = module_define.hxx_pb2._PBBASICPROPERTY
_PBTPLPETSKIN.fields_by_name['init_skill'].message_type = _PBTPLPETINITSKILL
DESCRIPTOR.message_types_by_name['PBTplPetInitSkill'] = _PBTPLPETINITSKILL
DESCRIPTOR.message_types_by_name['PBTplPetSkin'] = _PBTPLPETSKIN

PBTplPetInitSkill = _reflection.GeneratedProtocolMessageType('PBTplPetInitSkill', (_message.Message,), dict(
  DESCRIPTOR = _PBTPLPETINITSKILL,
  __module__ = 'pet_skin_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBTplPetInitSkill)
  ))
_sym_db.RegisterMessage(PBTplPetInitSkill)

PBTplPetSkin = _reflection.GeneratedProtocolMessageType('PBTplPetSkin', (_message.Message,), dict(
  DESCRIPTOR = _PBTPLPETSKIN,
  __module__ = 'pet_skin_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBTplPetSkin)
  ))
_sym_db.RegisterMessage(PBTplPetSkin)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

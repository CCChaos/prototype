# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goods_tpl.hxx

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
  name='goods_tpl.hxx',
  package='',
  serialized_pb=_b('\n\rgoods_tpl.hxx\"\xf3\x01\n\x12PBTplShopGoodsBase\x12\x1c\n\x14purchase_count_limit\x18\x01 \x01(\x05\x12(\n purchase_count_limit_single_time\x18\x02 \x01(\x05\x12\x14\n\x0cis_buy_limit\x18\x03 \x01(\x08\x12\x1b\n\x13is_single_buy_limit\x18\x04 \x01(\x08\x12\x13\n\x0bis_discount\x18\x05 \x01(\x08\x12$\n\x1c\x63onsume_list_before_discount\x18\x06 \x01(\t\x12\x11\n\tdrop_list\x18\x07 \x01(\t\x12\x14\n\x0c\x63onsume_list\x18\x08 \x01(\t\"E\n\x0ePBTplShopGoods\x12\n\n\x02id\x18\x01 \x01(\x05\x12\'\n\ngoods_base\x18\x02 \x01(\x0b\x32\x13.PBTplShopGoodsBaseB\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBTPLSHOPGOODSBASE = _descriptor.Descriptor(
  name='PBTplShopGoodsBase',
  full_name='PBTplShopGoodsBase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='purchase_count_limit', full_name='PBTplShopGoodsBase.purchase_count_limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='purchase_count_limit_single_time', full_name='PBTplShopGoodsBase.purchase_count_limit_single_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_buy_limit', full_name='PBTplShopGoodsBase.is_buy_limit', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_single_buy_limit', full_name='PBTplShopGoodsBase.is_single_buy_limit', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_discount', full_name='PBTplShopGoodsBase.is_discount', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume_list_before_discount', full_name='PBTplShopGoodsBase.consume_list_before_discount', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop_list', full_name='PBTplShopGoodsBase.drop_list', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume_list', full_name='PBTplShopGoodsBase.consume_list', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=18,
  serialized_end=261,
)


_PBTPLSHOPGOODS = _descriptor.Descriptor(
  name='PBTplShopGoods',
  full_name='PBTplShopGoods',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PBTplShopGoods.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods_base', full_name='PBTplShopGoods.goods_base', index=1,
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
  serialized_start=263,
  serialized_end=332,
)

_PBTPLSHOPGOODS.fields_by_name['goods_base'].message_type = _PBTPLSHOPGOODSBASE
DESCRIPTOR.message_types_by_name['PBTplShopGoodsBase'] = _PBTPLSHOPGOODSBASE
DESCRIPTOR.message_types_by_name['PBTplShopGoods'] = _PBTPLSHOPGOODS

PBTplShopGoodsBase = _reflection.GeneratedProtocolMessageType('PBTplShopGoodsBase', (_message.Message,), dict(
  DESCRIPTOR = _PBTPLSHOPGOODSBASE,
  __module__ = 'goods_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBTplShopGoodsBase)
  ))
_sym_db.RegisterMessage(PBTplShopGoodsBase)

PBTplShopGoods = _reflection.GeneratedProtocolMessageType('PBTplShopGoods', (_message.Message,), dict(
  DESCRIPTOR = _PBTPLSHOPGOODS,
  __module__ = 'goods_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBTplShopGoods)
  ))
_sym_db.RegisterMessage(PBTplShopGoods)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

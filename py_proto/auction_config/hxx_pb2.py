# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auction_config.hxx

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
  name='auction_config.hxx',
  package='',
  serialized_pb=_b('\n\x12\x61uction_config.hxx\"E\n\rPBAuctionItem\x12\x0e\n\x06tpl_id\x18\x01 \x01(\x05\x12\x11\n\tmin_price\x18\x02 \x01(\x05\x12\x11\n\tmax_price\x18\x03 \x01(\x05\";\n\rPBAuctionType\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x1c\n\x04item\x18\x02 \x03(\x0b\x32\x0e.PBAuctionItem\"/\n\tPBAuction\x12\"\n\ntrade_item\x18\x01 \x03(\x0b\x32\x0e.PBAuctionType\"\x89\x02\n\rPBTradeConfig\x12\x14\n\x0c\x63onsume_item\x18\x01 \x01(\x05\x12\x19\n\x11\x63onsume_sale_item\x18\x02 \x01(\x05\x12\x19\n\x11\x63onsume_sale_rate\x18\x03 \x01(\x05\x12\x18\n\x10\x63onsume_sale_min\x18\x04 \x01(\x05\x12\x15\n\rmax_sale_time\x18\x05 \x01(\x05\x12\x19\n\x11sale_consume_item\x18\x06 \x01(\x05\x12\x1c\n\x14sale_consume_itemnum\x18\x07 \x01(\x05\x12\x18\n\x10sale_consume_max\x18\x08 \x01(\x05\x12\x14\n\x0c\x63onsume_site\x18\t \x01(\x05\x12\x12\n\nforce_time\x18\n \x01(\x05\"T\n\nPBSiftItem\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0c\n\x04suit\x18\x02 \x01(\x05\x12\r\n\x05\x63lass\x18\x03 \x01(\x05\x12\r\n\x05start\x18\x04 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x05\"4\n\tPBSiftSet\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x19\n\x04item\x18\x02 \x03(\x0b\x32\x0b.PBSiftItem\"(\n\x0cPBSiftConfig\x12\x18\n\x04sift\x18\x01 \x03(\x0b\x32\n.PBSiftSet\"\x1f\n\rPBHotItemList\x12\x0e\n\x06tpl_id\x18\x01 \x01(\x05\")\n\tPBHotInfo\x12\x1c\n\x04item\x18\x01 \x03(\x0b\x32\x0e.PBHotItemList\"\x9b\x01\n\x11PBConfTradeConfig\x12$\n\x0ctrade_config\x18\x01 \x01(\x0b\x32\x0e.PBTradeConfig\x12\x1e\n\ntrade_info\x18\x02 \x01(\x0b\x32\n.PBAuction\x12\"\n\x0bsift_config\x18\x03 \x01(\x0b\x32\r.PBSiftConfig\x12\x1c\n\x08hot_item\x18\x04 \x01(\x0b\x32\n.PBHotInfoB\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBAUCTIONITEM = _descriptor.Descriptor(
  name='PBAuctionItem',
  full_name='PBAuctionItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tpl_id', full_name='PBAuctionItem.tpl_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_price', full_name='PBAuctionItem.min_price', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_price', full_name='PBAuctionItem.max_price', index=2,
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
  serialized_start=22,
  serialized_end=91,
)


_PBAUCTIONTYPE = _descriptor.Descriptor(
  name='PBAuctionType',
  full_name='PBAuctionType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='PBAuctionType.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='PBAuctionType.item', index=1,
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
  serialized_start=93,
  serialized_end=152,
)


_PBAUCTION = _descriptor.Descriptor(
  name='PBAuction',
  full_name='PBAuction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trade_item', full_name='PBAuction.trade_item', index=0,
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
  serialized_start=154,
  serialized_end=201,
)


_PBTRADECONFIG = _descriptor.Descriptor(
  name='PBTradeConfig',
  full_name='PBTradeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consume_item', full_name='PBTradeConfig.consume_item', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume_sale_item', full_name='PBTradeConfig.consume_sale_item', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume_sale_rate', full_name='PBTradeConfig.consume_sale_rate', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume_sale_min', full_name='PBTradeConfig.consume_sale_min', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_sale_time', full_name='PBTradeConfig.max_sale_time', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sale_consume_item', full_name='PBTradeConfig.sale_consume_item', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sale_consume_itemnum', full_name='PBTradeConfig.sale_consume_itemnum', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sale_consume_max', full_name='PBTradeConfig.sale_consume_max', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume_site', full_name='PBTradeConfig.consume_site', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='force_time', full_name='PBTradeConfig.force_time', index=9,
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
  serialized_start=204,
  serialized_end=469,
)


_PBSIFTITEM = _descriptor.Descriptor(
  name='PBSiftItem',
  full_name='PBSiftItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='PBSiftItem.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='suit', full_name='PBSiftItem.suit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class', full_name='PBSiftItem.class', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='PBSiftItem.start', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='PBSiftItem.end', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=471,
  serialized_end=555,
)


_PBSIFTSET = _descriptor.Descriptor(
  name='PBSiftSet',
  full_name='PBSiftSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='PBSiftSet.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='PBSiftSet.item', index=1,
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
  serialized_start=557,
  serialized_end=609,
)


_PBSIFTCONFIG = _descriptor.Descriptor(
  name='PBSiftConfig',
  full_name='PBSiftConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sift', full_name='PBSiftConfig.sift', index=0,
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
  serialized_start=611,
  serialized_end=651,
)


_PBHOTITEMLIST = _descriptor.Descriptor(
  name='PBHotItemList',
  full_name='PBHotItemList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tpl_id', full_name='PBHotItemList.tpl_id', index=0,
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
  serialized_start=653,
  serialized_end=684,
)


_PBHOTINFO = _descriptor.Descriptor(
  name='PBHotInfo',
  full_name='PBHotInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='PBHotInfo.item', index=0,
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
  serialized_start=686,
  serialized_end=727,
)


_PBCONFTRADECONFIG = _descriptor.Descriptor(
  name='PBConfTradeConfig',
  full_name='PBConfTradeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trade_config', full_name='PBConfTradeConfig.trade_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trade_info', full_name='PBConfTradeConfig.trade_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sift_config', full_name='PBConfTradeConfig.sift_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hot_item', full_name='PBConfTradeConfig.hot_item', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=730,
  serialized_end=885,
)

_PBAUCTIONTYPE.fields_by_name['item'].message_type = _PBAUCTIONITEM
_PBAUCTION.fields_by_name['trade_item'].message_type = _PBAUCTIONTYPE
_PBSIFTSET.fields_by_name['item'].message_type = _PBSIFTITEM
_PBSIFTCONFIG.fields_by_name['sift'].message_type = _PBSIFTSET
_PBHOTINFO.fields_by_name['item'].message_type = _PBHOTITEMLIST
_PBCONFTRADECONFIG.fields_by_name['trade_config'].message_type = _PBTRADECONFIG
_PBCONFTRADECONFIG.fields_by_name['trade_info'].message_type = _PBAUCTION
_PBCONFTRADECONFIG.fields_by_name['sift_config'].message_type = _PBSIFTCONFIG
_PBCONFTRADECONFIG.fields_by_name['hot_item'].message_type = _PBHOTINFO
DESCRIPTOR.message_types_by_name['PBAuctionItem'] = _PBAUCTIONITEM
DESCRIPTOR.message_types_by_name['PBAuctionType'] = _PBAUCTIONTYPE
DESCRIPTOR.message_types_by_name['PBAuction'] = _PBAUCTION
DESCRIPTOR.message_types_by_name['PBTradeConfig'] = _PBTRADECONFIG
DESCRIPTOR.message_types_by_name['PBSiftItem'] = _PBSIFTITEM
DESCRIPTOR.message_types_by_name['PBSiftSet'] = _PBSIFTSET
DESCRIPTOR.message_types_by_name['PBSiftConfig'] = _PBSIFTCONFIG
DESCRIPTOR.message_types_by_name['PBHotItemList'] = _PBHOTITEMLIST
DESCRIPTOR.message_types_by_name['PBHotInfo'] = _PBHOTINFO
DESCRIPTOR.message_types_by_name['PBConfTradeConfig'] = _PBCONFTRADECONFIG

PBAuctionItem = _reflection.GeneratedProtocolMessageType('PBAuctionItem', (_message.Message,), dict(
  DESCRIPTOR = _PBAUCTIONITEM,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBAuctionItem)
  ))
_sym_db.RegisterMessage(PBAuctionItem)

PBAuctionType = _reflection.GeneratedProtocolMessageType('PBAuctionType', (_message.Message,), dict(
  DESCRIPTOR = _PBAUCTIONTYPE,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBAuctionType)
  ))
_sym_db.RegisterMessage(PBAuctionType)

PBAuction = _reflection.GeneratedProtocolMessageType('PBAuction', (_message.Message,), dict(
  DESCRIPTOR = _PBAUCTION,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBAuction)
  ))
_sym_db.RegisterMessage(PBAuction)

PBTradeConfig = _reflection.GeneratedProtocolMessageType('PBTradeConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBTRADECONFIG,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBTradeConfig)
  ))
_sym_db.RegisterMessage(PBTradeConfig)

PBSiftItem = _reflection.GeneratedProtocolMessageType('PBSiftItem', (_message.Message,), dict(
  DESCRIPTOR = _PBSIFTITEM,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBSiftItem)
  ))
_sym_db.RegisterMessage(PBSiftItem)

PBSiftSet = _reflection.GeneratedProtocolMessageType('PBSiftSet', (_message.Message,), dict(
  DESCRIPTOR = _PBSIFTSET,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBSiftSet)
  ))
_sym_db.RegisterMessage(PBSiftSet)

PBSiftConfig = _reflection.GeneratedProtocolMessageType('PBSiftConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBSIFTCONFIG,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBSiftConfig)
  ))
_sym_db.RegisterMessage(PBSiftConfig)

PBHotItemList = _reflection.GeneratedProtocolMessageType('PBHotItemList', (_message.Message,), dict(
  DESCRIPTOR = _PBHOTITEMLIST,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBHotItemList)
  ))
_sym_db.RegisterMessage(PBHotItemList)

PBHotInfo = _reflection.GeneratedProtocolMessageType('PBHotInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBHOTINFO,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBHotInfo)
  ))
_sym_db.RegisterMessage(PBHotInfo)

PBConfTradeConfig = _reflection.GeneratedProtocolMessageType('PBConfTradeConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBCONFTRADECONFIG,
  __module__ = 'auction_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBConfTradeConfig)
  ))
_sym_db.RegisterMessage(PBConfTradeConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

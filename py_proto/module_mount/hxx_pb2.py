# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_mount.hxx

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import module_scene.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='module_mount.hxx',
  package='',
  serialized_pb=_b('\n\x10module_mount.hxx\x1a\x10module_scene.hxx\"@\n\x07PBMount\x12\x10\n\x08mount_id\x18\x01 \x01(\x05\x12\x13\n\x0bmount_power\x18\x02 \x01(\x05\x12\x0e\n\x06unlock\x18\x03 \x01(\x08\"$\n\x13PBMsgC2SRideRequest\x12\r\n\x05mount\x18\x01 \x01(\x08\"9\n\x14PBMsgS2CRideResponse\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x10\n\x08mount_id\x18\x02 \x01(\x05\",\n\x18PBMsgC2SMountRideRequest\x12\x10\n\x08mount_id\x18\x01 \x01(\x05\"P\n\x19PBMsgS2CMountRideResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x12\x10\n\x08mount_id\x18\x02 \x01(\x05\x12\x0f\n\x07last_cd\x18\x03 \x01(\x05\"\x19\n\x17PBMsgC2SMountStopReport\"\x19\n\x17PBMsgS2CMountStopNotice\"\x1a\n\x18PBMsgC2SMountRestRequest\"C\n\x19PBMsgS2CMountRestResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01z\x18\x03 \x01(\x05\"0\n\x1cPBMsgC2SMountActivateRequest\x12\x10\n\x08mount_id\x18\x01 \x01(\x05\"C\n\x1dPBMsgS2CMountActivateResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x12\x10\n\x08mount_id\x18\x02 \x01(\x05\"W\n\x1bPBMsgS2CMountActivateNotice\x12\x19\n\x11\x61\x63tivate_mount_id\x18\x01 \x01(\x05\x12\x1d\n\x06status\x18\x02 \x01(\x0e\x32\r.EMountStatus\"\x1a\n\x18PBMsgC2SMountInfoRequest\"K\n\x19PBMsgS2CMountInfoResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x12\x1c\n\nmount_list\x18\x02 \x03(\x0b\x32\x08.PBMount\"C\n\"PBMsgC2SMountChangeSkyLayerRequest\x12\x1d\n\x05layer\x18\x01 \x01(\x0e\x32\x0e.PBEntityLayer\"V\n#PBMsgS2CMountChangeSkyLayerResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x12\x1d\n\x05layer\x18\x02 \x01(\x0e\x32\x0e.PBEntityLayer\".\n\x1aPBMsgC2SMountUnlockRequest\x12\x10\n\x08mount_id\x18\x01 \x01(\x05\"A\n\x1bPBMsgS2CMountUnlockResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x12\x10\n\x08mount_id\x18\x02 \x01(\x05*\xd8\x04\n\x12MSGID_MODULE_MOUNT\x12\x1a\n\x15ID_MOUNT_RIDE_REQUEST\x10\x80\x0c\x12\x1b\n\x16ID_MOUNT_RIDE_RESPONSE\x10\x81\x0c\x12\x1e\n\x19ID_C2S_MOUNT_RIDE_REQUEST\x10\x82\x0c\x12\x1f\n\x1aID_S2C_MOUNT_RIDE_RESPONSE\x10\x83\x0c\x12\x1d\n\x18ID_C2S_MOUNT_STOP_REPORT\x10\x84\x0c\x12\x1e\n\x19ID_C2S_MOUNT_REST_REQUEST\x10\x85\x0c\x12\x1f\n\x1aID_S2C_MOUNT_REST_RESPONSE\x10\x86\x0c\x12\"\n\x1dID_C2S_MOUNT_ACTIVATE_REQUEST\x10\x87\x0c\x12#\n\x1eID_S2C_MOUNT_ACTIVATE_RESPONSE\x10\x88\x0c\x12!\n\x1cID_S2C_MOUNT_ACTIVATE_NOTICE\x10\x89\x0c\x12\x1e\n\x19ID_C2S_MOUNT_INFO_REQUEST\x10\x8a\x0c\x12\x1f\n\x1aID_S2C_MOUNT_INFO_RESPONSE\x10\x8b\x0c\x12\x1d\n\x18ID_S2C_MOUNT_STOP_NOTICE\x10\x8c\x0c\x12*\n%ID_C2S_MOUNT_CHANGE_SKY_LAYER_REQUEST\x10\x8d\x0c\x12+\n&ID_S2C_MOUNT_CHANGE_SKY_LAYER_RESPONSE\x10\x8e\x0c\x12 \n\x1bID_C2S_MOUNT_UNLOCK_REQUEST\x10\x8f\x0c\x12!\n\x1cID_S2C_MOUNT_UNLOCK_RESPONSE\x10\x90\x0c*F\n\x0f\x45MountLayerType\x12\x1a\n\x16MOUNT_LAYERTYPE_GROUND\x10\x01\x12\x17\n\x13MOUNT_LAYERTYPE_SKY\x10\x02*o\n\x0c\x45MountStatus\x12\x15\n\x11MOUNT_STATUS_REST\x10\x00\x12\x19\n\x15MOUNT_STATUS_ACTIVATE\x10\x01\x12\x16\n\x12MOUNT_STATUS_CDING\x10\x02\x12\x15\n\x11MOUNT_STATUS_RIDE\x10\x03\x42\x02H\x01')
  ,
  dependencies=[module_scene.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGID_MODULE_MOUNT = _descriptor.EnumDescriptor(
  name='MSGID_MODULE_MOUNT',
  full_name='MSGID_MODULE_MOUNT',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ID_MOUNT_RIDE_REQUEST', index=0, number=1536,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_MOUNT_RIDE_RESPONSE', index=1, number=1537,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_MOUNT_RIDE_REQUEST', index=2, number=1538,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_MOUNT_RIDE_RESPONSE', index=3, number=1539,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_MOUNT_STOP_REPORT', index=4, number=1540,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_MOUNT_REST_REQUEST', index=5, number=1541,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_MOUNT_REST_RESPONSE', index=6, number=1542,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_MOUNT_ACTIVATE_REQUEST', index=7, number=1543,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_MOUNT_ACTIVATE_RESPONSE', index=8, number=1544,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_MOUNT_ACTIVATE_NOTICE', index=9, number=1545,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_MOUNT_INFO_REQUEST', index=10, number=1546,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_MOUNT_INFO_RESPONSE', index=11, number=1547,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_MOUNT_STOP_NOTICE', index=12, number=1548,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_MOUNT_CHANGE_SKY_LAYER_REQUEST', index=13, number=1549,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_MOUNT_CHANGE_SKY_LAYER_RESPONSE', index=14, number=1550,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_C2S_MOUNT_UNLOCK_REQUEST', index=15, number=1551,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_S2C_MOUNT_UNLOCK_RESPONSE', index=16, number=1552,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1066,
  serialized_end=1666,
)
_sym_db.RegisterEnumDescriptor(_MSGID_MODULE_MOUNT)

MSGID_MODULE_MOUNT = enum_type_wrapper.EnumTypeWrapper(_MSGID_MODULE_MOUNT)
_EMOUNTLAYERTYPE = _descriptor.EnumDescriptor(
  name='EMountLayerType',
  full_name='EMountLayerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOUNT_LAYERTYPE_GROUND', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOUNT_LAYERTYPE_SKY', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1668,
  serialized_end=1738,
)
_sym_db.RegisterEnumDescriptor(_EMOUNTLAYERTYPE)

EMountLayerType = enum_type_wrapper.EnumTypeWrapper(_EMOUNTLAYERTYPE)
_EMOUNTSTATUS = _descriptor.EnumDescriptor(
  name='EMountStatus',
  full_name='EMountStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOUNT_STATUS_REST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOUNT_STATUS_ACTIVATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOUNT_STATUS_CDING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOUNT_STATUS_RIDE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1740,
  serialized_end=1851,
)
_sym_db.RegisterEnumDescriptor(_EMOUNTSTATUS)

EMountStatus = enum_type_wrapper.EnumTypeWrapper(_EMOUNTSTATUS)
ID_MOUNT_RIDE_REQUEST = 1536
ID_MOUNT_RIDE_RESPONSE = 1537
ID_C2S_MOUNT_RIDE_REQUEST = 1538
ID_S2C_MOUNT_RIDE_RESPONSE = 1539
ID_C2S_MOUNT_STOP_REPORT = 1540
ID_C2S_MOUNT_REST_REQUEST = 1541
ID_S2C_MOUNT_REST_RESPONSE = 1542
ID_C2S_MOUNT_ACTIVATE_REQUEST = 1543
ID_S2C_MOUNT_ACTIVATE_RESPONSE = 1544
ID_S2C_MOUNT_ACTIVATE_NOTICE = 1545
ID_C2S_MOUNT_INFO_REQUEST = 1546
ID_S2C_MOUNT_INFO_RESPONSE = 1547
ID_S2C_MOUNT_STOP_NOTICE = 1548
ID_C2S_MOUNT_CHANGE_SKY_LAYER_REQUEST = 1549
ID_S2C_MOUNT_CHANGE_SKY_LAYER_RESPONSE = 1550
ID_C2S_MOUNT_UNLOCK_REQUEST = 1551
ID_S2C_MOUNT_UNLOCK_RESPONSE = 1552
MOUNT_LAYERTYPE_GROUND = 1
MOUNT_LAYERTYPE_SKY = 2
MOUNT_STATUS_REST = 0
MOUNT_STATUS_ACTIVATE = 1
MOUNT_STATUS_CDING = 2
MOUNT_STATUS_RIDE = 3



_PBMOUNT = _descriptor.Descriptor(
  name='PBMount',
  full_name='PBMount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount_id', full_name='PBMount.mount_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_power', full_name='PBMount.mount_power', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unlock', full_name='PBMount.unlock', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=38,
  serialized_end=102,
)


_PBMSGC2SRIDEREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SRideRequest',
  full_name='PBMsgC2SRideRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount', full_name='PBMsgC2SRideRequest.mount', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=104,
  serialized_end=140,
)


_PBMSGS2CRIDERESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CRideResponse',
  full_name='PBMsgS2CRideResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retcode', full_name='PBMsgS2CRideResponse.retcode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_id', full_name='PBMsgS2CRideResponse.mount_id', index=1,
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
  serialized_start=142,
  serialized_end=199,
)


_PBMSGC2SMOUNTRIDEREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SMountRideRequest',
  full_name='PBMsgC2SMountRideRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount_id', full_name='PBMsgC2SMountRideRequest.mount_id', index=0,
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
  serialized_start=201,
  serialized_end=245,
)


_PBMSGS2CMOUNTRIDERESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CMountRideResponse',
  full_name='PBMsgS2CMountRideResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgS2CMountRideResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_id', full_name='PBMsgS2CMountRideResponse.mount_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_cd', full_name='PBMsgS2CMountRideResponse.last_cd', index=2,
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
  serialized_start=247,
  serialized_end=327,
)


_PBMSGC2SMOUNTSTOPREPORT = _descriptor.Descriptor(
  name='PBMsgC2SMountStopReport',
  full_name='PBMsgC2SMountStopReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=329,
  serialized_end=354,
)


_PBMSGS2CMOUNTSTOPNOTICE = _descriptor.Descriptor(
  name='PBMsgS2CMountStopNotice',
  full_name='PBMsgS2CMountStopNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=356,
  serialized_end=381,
)


_PBMSGC2SMOUNTRESTREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SMountRestRequest',
  full_name='PBMsgC2SMountRestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=383,
  serialized_end=409,
)


_PBMSGS2CMOUNTRESTRESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CMountRestResponse',
  full_name='PBMsgS2CMountRestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgS2CMountRestResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='PBMsgS2CMountRestResponse.x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='PBMsgS2CMountRestResponse.z', index=2,
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
  serialized_start=411,
  serialized_end=478,
)


_PBMSGC2SMOUNTACTIVATEREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SMountActivateRequest',
  full_name='PBMsgC2SMountActivateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount_id', full_name='PBMsgC2SMountActivateRequest.mount_id', index=0,
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
  serialized_start=480,
  serialized_end=528,
)


_PBMSGS2CMOUNTACTIVATERESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CMountActivateResponse',
  full_name='PBMsgS2CMountActivateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgS2CMountActivateResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_id', full_name='PBMsgS2CMountActivateResponse.mount_id', index=1,
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
  serialized_start=530,
  serialized_end=597,
)


_PBMSGS2CMOUNTACTIVATENOTICE = _descriptor.Descriptor(
  name='PBMsgS2CMountActivateNotice',
  full_name='PBMsgS2CMountActivateNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activate_mount_id', full_name='PBMsgS2CMountActivateNotice.activate_mount_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='PBMsgS2CMountActivateNotice.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=599,
  serialized_end=686,
)


_PBMSGC2SMOUNTINFOREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SMountInfoRequest',
  full_name='PBMsgC2SMountInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=688,
  serialized_end=714,
)


_PBMSGS2CMOUNTINFORESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CMountInfoResponse',
  full_name='PBMsgS2CMountInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgS2CMountInfoResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_list', full_name='PBMsgS2CMountInfoResponse.mount_list', index=1,
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
  serialized_start=716,
  serialized_end=791,
)


_PBMSGC2SMOUNTCHANGESKYLAYERREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SMountChangeSkyLayerRequest',
  full_name='PBMsgC2SMountChangeSkyLayerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layer', full_name='PBMsgC2SMountChangeSkyLayerRequest.layer', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=793,
  serialized_end=860,
)


_PBMSGS2CMOUNTCHANGESKYLAYERRESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CMountChangeSkyLayerResponse',
  full_name='PBMsgS2CMountChangeSkyLayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgS2CMountChangeSkyLayerResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layer', full_name='PBMsgS2CMountChangeSkyLayerResponse.layer', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=862,
  serialized_end=948,
)


_PBMSGC2SMOUNTUNLOCKREQUEST = _descriptor.Descriptor(
  name='PBMsgC2SMountUnlockRequest',
  full_name='PBMsgC2SMountUnlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount_id', full_name='PBMsgC2SMountUnlockRequest.mount_id', index=0,
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
  serialized_start=950,
  serialized_end=996,
)


_PBMSGS2CMOUNTUNLOCKRESPONSE = _descriptor.Descriptor(
  name='PBMsgS2CMountUnlockResponse',
  full_name='PBMsgS2CMountUnlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgS2CMountUnlockResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mount_id', full_name='PBMsgS2CMountUnlockResponse.mount_id', index=1,
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
  serialized_start=998,
  serialized_end=1063,
)

_PBMSGS2CMOUNTACTIVATENOTICE.fields_by_name['status'].enum_type = _EMOUNTSTATUS
_PBMSGS2CMOUNTINFORESPONSE.fields_by_name['mount_list'].message_type = _PBMOUNT
_PBMSGC2SMOUNTCHANGESKYLAYERREQUEST.fields_by_name['layer'].enum_type = module_scene.hxx_pb2._PBENTITYLAYER
_PBMSGS2CMOUNTCHANGESKYLAYERRESPONSE.fields_by_name['layer'].enum_type = module_scene.hxx_pb2._PBENTITYLAYER
DESCRIPTOR.message_types_by_name['PBMount'] = _PBMOUNT
DESCRIPTOR.message_types_by_name['PBMsgC2SRideRequest'] = _PBMSGC2SRIDEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CRideResponse'] = _PBMSGS2CRIDERESPONSE
DESCRIPTOR.message_types_by_name['PBMsgC2SMountRideRequest'] = _PBMSGC2SMOUNTRIDEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CMountRideResponse'] = _PBMSGS2CMOUNTRIDERESPONSE
DESCRIPTOR.message_types_by_name['PBMsgC2SMountStopReport'] = _PBMSGC2SMOUNTSTOPREPORT
DESCRIPTOR.message_types_by_name['PBMsgS2CMountStopNotice'] = _PBMSGS2CMOUNTSTOPNOTICE
DESCRIPTOR.message_types_by_name['PBMsgC2SMountRestRequest'] = _PBMSGC2SMOUNTRESTREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CMountRestResponse'] = _PBMSGS2CMOUNTRESTRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgC2SMountActivateRequest'] = _PBMSGC2SMOUNTACTIVATEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CMountActivateResponse'] = _PBMSGS2CMOUNTACTIVATERESPONSE
DESCRIPTOR.message_types_by_name['PBMsgS2CMountActivateNotice'] = _PBMSGS2CMOUNTACTIVATENOTICE
DESCRIPTOR.message_types_by_name['PBMsgC2SMountInfoRequest'] = _PBMSGC2SMOUNTINFOREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CMountInfoResponse'] = _PBMSGS2CMOUNTINFORESPONSE
DESCRIPTOR.message_types_by_name['PBMsgC2SMountChangeSkyLayerRequest'] = _PBMSGC2SMOUNTCHANGESKYLAYERREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CMountChangeSkyLayerResponse'] = _PBMSGS2CMOUNTCHANGESKYLAYERRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgC2SMountUnlockRequest'] = _PBMSGC2SMOUNTUNLOCKREQUEST
DESCRIPTOR.message_types_by_name['PBMsgS2CMountUnlockResponse'] = _PBMSGS2CMOUNTUNLOCKRESPONSE
DESCRIPTOR.enum_types_by_name['MSGID_MODULE_MOUNT'] = _MSGID_MODULE_MOUNT
DESCRIPTOR.enum_types_by_name['EMountLayerType'] = _EMOUNTLAYERTYPE
DESCRIPTOR.enum_types_by_name['EMountStatus'] = _EMOUNTSTATUS

PBMount = _reflection.GeneratedProtocolMessageType('PBMount', (_message.Message,), dict(
  DESCRIPTOR = _PBMOUNT,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMount)
  ))
_sym_db.RegisterMessage(PBMount)

PBMsgC2SRideRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SRideRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SRIDEREQUEST,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SRideRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SRideRequest)

PBMsgS2CRideResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CRideResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CRIDERESPONSE,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CRideResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CRideResponse)

PBMsgC2SMountRideRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SMountRideRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SMOUNTRIDEREQUEST,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SMountRideRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SMountRideRequest)

PBMsgS2CMountRideResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CMountRideResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CMOUNTRIDERESPONSE,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CMountRideResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CMountRideResponse)

PBMsgC2SMountStopReport = _reflection.GeneratedProtocolMessageType('PBMsgC2SMountStopReport', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SMOUNTSTOPREPORT,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SMountStopReport)
  ))
_sym_db.RegisterMessage(PBMsgC2SMountStopReport)

PBMsgS2CMountStopNotice = _reflection.GeneratedProtocolMessageType('PBMsgS2CMountStopNotice', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CMOUNTSTOPNOTICE,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CMountStopNotice)
  ))
_sym_db.RegisterMessage(PBMsgS2CMountStopNotice)

PBMsgC2SMountRestRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SMountRestRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SMOUNTRESTREQUEST,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SMountRestRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SMountRestRequest)

PBMsgS2CMountRestResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CMountRestResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CMOUNTRESTRESPONSE,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CMountRestResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CMountRestResponse)

PBMsgC2SMountActivateRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SMountActivateRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SMOUNTACTIVATEREQUEST,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SMountActivateRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SMountActivateRequest)

PBMsgS2CMountActivateResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CMountActivateResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CMOUNTACTIVATERESPONSE,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CMountActivateResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CMountActivateResponse)

PBMsgS2CMountActivateNotice = _reflection.GeneratedProtocolMessageType('PBMsgS2CMountActivateNotice', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CMOUNTACTIVATENOTICE,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CMountActivateNotice)
  ))
_sym_db.RegisterMessage(PBMsgS2CMountActivateNotice)

PBMsgC2SMountInfoRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SMountInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SMOUNTINFOREQUEST,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SMountInfoRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SMountInfoRequest)

PBMsgS2CMountInfoResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CMountInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CMOUNTINFORESPONSE,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CMountInfoResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CMountInfoResponse)

PBMsgC2SMountChangeSkyLayerRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SMountChangeSkyLayerRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SMOUNTCHANGESKYLAYERREQUEST,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SMountChangeSkyLayerRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SMountChangeSkyLayerRequest)

PBMsgS2CMountChangeSkyLayerResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CMountChangeSkyLayerResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CMOUNTCHANGESKYLAYERRESPONSE,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CMountChangeSkyLayerResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CMountChangeSkyLayerResponse)

PBMsgC2SMountUnlockRequest = _reflection.GeneratedProtocolMessageType('PBMsgC2SMountUnlockRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGC2SMOUNTUNLOCKREQUEST,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgC2SMountUnlockRequest)
  ))
_sym_db.RegisterMessage(PBMsgC2SMountUnlockRequest)

PBMsgS2CMountUnlockResponse = _reflection.GeneratedProtocolMessageType('PBMsgS2CMountUnlockResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2CMOUNTUNLOCKRESPONSE,
  __module__ = 'module_mount.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2CMountUnlockResponse)
  ))
_sym_db.RegisterMessage(PBMsgS2CMountUnlockResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_gm.hxx

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
  name='msg_gm.hxx',
  package='',
  serialized_pb=_b('\n\nmsg_gm.hxx\"L\n\x1aPBMsgGMCmdGeneralResultRes\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x0e\n\x06result\x18\x03 \x01(\x05\"W\n!PBMsgL2GGMCmdFreezeAccountRequest\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x12\n\naccount_id\x18\x03 \x01(\x05\"U\n\x1fPBMsgL2GGMCmdUnFreezeAccountReq\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x12\n\naccount_id\x18\x03 \x01(\x05\"O\n\x1cPBMsgL2GGMCmdKickRoleRequest\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\"n\n\x1aPBMsgL2GGMCmdShutupRequest\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\x12\x0e\n\x06period\x18\x05 \x01(\x05\"m\n\x19PBMsgG2SGMCmdShutupNotify\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\x12\x0e\n\x06period\x18\x05 \x01(\x05\"m\n\x19PBMsgG2DGMCmdShutupNotify\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\x12\x0e\n\x06period\x18\x05 \x01(\x05\"t\n PBMsgL2GGMCmdCancelShutupRequest\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\x12\x0e\n\x06period\x18\x05 \x01(\x05\"c\n\x1fPBMsgG2SGMCmdCancelShutupNotify\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\"c\n\x1fPBMsgG2DGMCmdCancelShutupNotify\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\">\n\x1fPBMsgL2GGmCmdRecoverRoleRequest\x12\n\n\x02\x66\x64\x18\x01 \x01(\r\x12\x0f\n\x07role_id\x18\x02 \x01(\r\"I\n\x16PBMsgL2GGMCmdNoticeReq\x12\x12\n\nsession_id\x18\x01 \x01(\r\x12\n\n\x02\x66\x64\x18\x02 \x01(\r\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"?\n\x1bPBMsgS2GDebugCommandRequest\x12\x0f\n\x07role_id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\"+\n\x18PBMsgG2SChangeTimeNotify\x12\x0f\n\x07\x63ur_sec\x18\x01 \x01(\x03\x42\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBMSGGMCMDGENERALRESULTRES = _descriptor.Descriptor(
  name='PBMsgGMCmdGeneralResultRes',
  full_name='PBMsgGMCmdGeneralResultRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgGMCmdGeneralResultRes.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgGMCmdGeneralResultRes.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='PBMsgGMCmdGeneralResultRes.result', index=2,
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
  serialized_start=14,
  serialized_end=90,
)


_PBMSGL2GGMCMDFREEZEACCOUNTREQUEST = _descriptor.Descriptor(
  name='PBMsgL2GGMCmdFreezeAccountRequest',
  full_name='PBMsgL2GGMCmdFreezeAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgL2GGMCmdFreezeAccountRequest.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgL2GGMCmdFreezeAccountRequest.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='PBMsgL2GGMCmdFreezeAccountRequest.account_id', index=2,
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
  serialized_start=92,
  serialized_end=179,
)


_PBMSGL2GGMCMDUNFREEZEACCOUNTREQ = _descriptor.Descriptor(
  name='PBMsgL2GGMCmdUnFreezeAccountReq',
  full_name='PBMsgL2GGMCmdUnFreezeAccountReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgL2GGMCmdUnFreezeAccountReq.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgL2GGMCmdUnFreezeAccountReq.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='PBMsgL2GGMCmdUnFreezeAccountReq.account_id', index=2,
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
  serialized_start=181,
  serialized_end=266,
)


_PBMSGL2GGMCMDKICKROLEREQUEST = _descriptor.Descriptor(
  name='PBMsgL2GGMCmdKickRoleRequest',
  full_name='PBMsgL2GGMCmdKickRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgL2GGMCmdKickRoleRequest.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgL2GGMCmdKickRoleRequest.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgL2GGMCmdKickRoleRequest.role_id', index=2,
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
  serialized_start=268,
  serialized_end=347,
)


_PBMSGL2GGMCMDSHUTUPREQUEST = _descriptor.Descriptor(
  name='PBMsgL2GGMCmdShutupRequest',
  full_name='PBMsgL2GGMCmdShutupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgL2GGMCmdShutupRequest.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgL2GGMCmdShutupRequest.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgL2GGMCmdShutupRequest.role_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='PBMsgL2GGMCmdShutupRequest.channel', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='period', full_name='PBMsgL2GGMCmdShutupRequest.period', index=4,
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
  serialized_start=349,
  serialized_end=459,
)


_PBMSGG2SGMCMDSHUTUPNOTIFY = _descriptor.Descriptor(
  name='PBMsgG2SGMCmdShutupNotify',
  full_name='PBMsgG2SGMCmdShutupNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgG2SGMCmdShutupNotify.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgG2SGMCmdShutupNotify.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgG2SGMCmdShutupNotify.role_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='PBMsgG2SGMCmdShutupNotify.channel', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='period', full_name='PBMsgG2SGMCmdShutupNotify.period', index=4,
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
  serialized_start=461,
  serialized_end=570,
)


_PBMSGG2DGMCMDSHUTUPNOTIFY = _descriptor.Descriptor(
  name='PBMsgG2DGMCmdShutupNotify',
  full_name='PBMsgG2DGMCmdShutupNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgG2DGMCmdShutupNotify.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgG2DGMCmdShutupNotify.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgG2DGMCmdShutupNotify.role_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='PBMsgG2DGMCmdShutupNotify.channel', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='period', full_name='PBMsgG2DGMCmdShutupNotify.period', index=4,
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
  serialized_start=572,
  serialized_end=681,
)


_PBMSGL2GGMCMDCANCELSHUTUPREQUEST = _descriptor.Descriptor(
  name='PBMsgL2GGMCmdCancelShutupRequest',
  full_name='PBMsgL2GGMCmdCancelShutupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgL2GGMCmdCancelShutupRequest.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgL2GGMCmdCancelShutupRequest.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgL2GGMCmdCancelShutupRequest.role_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='PBMsgL2GGMCmdCancelShutupRequest.channel', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='period', full_name='PBMsgL2GGMCmdCancelShutupRequest.period', index=4,
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
  serialized_start=683,
  serialized_end=799,
)


_PBMSGG2SGMCMDCANCELSHUTUPNOTIFY = _descriptor.Descriptor(
  name='PBMsgG2SGMCmdCancelShutupNotify',
  full_name='PBMsgG2SGMCmdCancelShutupNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgG2SGMCmdCancelShutupNotify.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgG2SGMCmdCancelShutupNotify.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgG2SGMCmdCancelShutupNotify.role_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='PBMsgG2SGMCmdCancelShutupNotify.channel', index=3,
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
  serialized_start=801,
  serialized_end=900,
)


_PBMSGG2DGMCMDCANCELSHUTUPNOTIFY = _descriptor.Descriptor(
  name='PBMsgG2DGMCmdCancelShutupNotify',
  full_name='PBMsgG2DGMCmdCancelShutupNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgG2DGMCmdCancelShutupNotify.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgG2DGMCmdCancelShutupNotify.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgG2DGMCmdCancelShutupNotify.role_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='PBMsgG2DGMCmdCancelShutupNotify.channel', index=3,
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
  serialized_start=902,
  serialized_end=1001,
)


_PBMSGL2GGMCMDRECOVERROLEREQUEST = _descriptor.Descriptor(
  name='PBMsgL2GGmCmdRecoverRoleRequest',
  full_name='PBMsgL2GGmCmdRecoverRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgL2GGmCmdRecoverRoleRequest.fd', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgL2GGmCmdRecoverRoleRequest.role_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=1003,
  serialized_end=1065,
)


_PBMSGL2GGMCMDNOTICEREQ = _descriptor.Descriptor(
  name='PBMsgL2GGMCmdNoticeReq',
  full_name='PBMsgL2GGMCmdNoticeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='PBMsgL2GGMCmdNoticeReq.session_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fd', full_name='PBMsgL2GGMCmdNoticeReq.fd', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='PBMsgL2GGMCmdNoticeReq.content', index=2,
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
  serialized_start=1067,
  serialized_end=1140,
)


_PBMSGS2GDEBUGCOMMANDREQUEST = _descriptor.Descriptor(
  name='PBMsgS2GDebugCommandRequest',
  full_name='PBMsgS2GDebugCommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgS2GDebugCommandRequest.role_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command', full_name='PBMsgS2GDebugCommandRequest.command', index=1,
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
  serialized_start=1142,
  serialized_end=1205,
)


_PBMSGG2SCHANGETIMENOTIFY = _descriptor.Descriptor(
  name='PBMsgG2SChangeTimeNotify',
  full_name='PBMsgG2SChangeTimeNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cur_sec', full_name='PBMsgG2SChangeTimeNotify.cur_sec', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=1207,
  serialized_end=1250,
)

DESCRIPTOR.message_types_by_name['PBMsgGMCmdGeneralResultRes'] = _PBMSGGMCMDGENERALRESULTRES
DESCRIPTOR.message_types_by_name['PBMsgL2GGMCmdFreezeAccountRequest'] = _PBMSGL2GGMCMDFREEZEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['PBMsgL2GGMCmdUnFreezeAccountReq'] = _PBMSGL2GGMCMDUNFREEZEACCOUNTREQ
DESCRIPTOR.message_types_by_name['PBMsgL2GGMCmdKickRoleRequest'] = _PBMSGL2GGMCMDKICKROLEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgL2GGMCmdShutupRequest'] = _PBMSGL2GGMCMDSHUTUPREQUEST
DESCRIPTOR.message_types_by_name['PBMsgG2SGMCmdShutupNotify'] = _PBMSGG2SGMCMDSHUTUPNOTIFY
DESCRIPTOR.message_types_by_name['PBMsgG2DGMCmdShutupNotify'] = _PBMSGG2DGMCMDSHUTUPNOTIFY
DESCRIPTOR.message_types_by_name['PBMsgL2GGMCmdCancelShutupRequest'] = _PBMSGL2GGMCMDCANCELSHUTUPREQUEST
DESCRIPTOR.message_types_by_name['PBMsgG2SGMCmdCancelShutupNotify'] = _PBMSGG2SGMCMDCANCELSHUTUPNOTIFY
DESCRIPTOR.message_types_by_name['PBMsgG2DGMCmdCancelShutupNotify'] = _PBMSGG2DGMCMDCANCELSHUTUPNOTIFY
DESCRIPTOR.message_types_by_name['PBMsgL2GGmCmdRecoverRoleRequest'] = _PBMSGL2GGMCMDRECOVERROLEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgL2GGMCmdNoticeReq'] = _PBMSGL2GGMCMDNOTICEREQ
DESCRIPTOR.message_types_by_name['PBMsgS2GDebugCommandRequest'] = _PBMSGS2GDEBUGCOMMANDREQUEST
DESCRIPTOR.message_types_by_name['PBMsgG2SChangeTimeNotify'] = _PBMSGG2SCHANGETIMENOTIFY

PBMsgGMCmdGeneralResultRes = _reflection.GeneratedProtocolMessageType('PBMsgGMCmdGeneralResultRes', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGGMCMDGENERALRESULTRES,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgGMCmdGeneralResultRes)
  ))
_sym_db.RegisterMessage(PBMsgGMCmdGeneralResultRes)

PBMsgL2GGMCmdFreezeAccountRequest = _reflection.GeneratedProtocolMessageType('PBMsgL2GGMCmdFreezeAccountRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGL2GGMCMDFREEZEACCOUNTREQUEST,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgL2GGMCmdFreezeAccountRequest)
  ))
_sym_db.RegisterMessage(PBMsgL2GGMCmdFreezeAccountRequest)

PBMsgL2GGMCmdUnFreezeAccountReq = _reflection.GeneratedProtocolMessageType('PBMsgL2GGMCmdUnFreezeAccountReq', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGL2GGMCMDUNFREEZEACCOUNTREQ,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgL2GGMCmdUnFreezeAccountReq)
  ))
_sym_db.RegisterMessage(PBMsgL2GGMCmdUnFreezeAccountReq)

PBMsgL2GGMCmdKickRoleRequest = _reflection.GeneratedProtocolMessageType('PBMsgL2GGMCmdKickRoleRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGL2GGMCMDKICKROLEREQUEST,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgL2GGMCmdKickRoleRequest)
  ))
_sym_db.RegisterMessage(PBMsgL2GGMCmdKickRoleRequest)

PBMsgL2GGMCmdShutupRequest = _reflection.GeneratedProtocolMessageType('PBMsgL2GGMCmdShutupRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGL2GGMCMDSHUTUPREQUEST,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgL2GGMCmdShutupRequest)
  ))
_sym_db.RegisterMessage(PBMsgL2GGMCmdShutupRequest)

PBMsgG2SGMCmdShutupNotify = _reflection.GeneratedProtocolMessageType('PBMsgG2SGMCmdShutupNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2SGMCMDSHUTUPNOTIFY,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2SGMCmdShutupNotify)
  ))
_sym_db.RegisterMessage(PBMsgG2SGMCmdShutupNotify)

PBMsgG2DGMCmdShutupNotify = _reflection.GeneratedProtocolMessageType('PBMsgG2DGMCmdShutupNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2DGMCMDSHUTUPNOTIFY,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2DGMCmdShutupNotify)
  ))
_sym_db.RegisterMessage(PBMsgG2DGMCmdShutupNotify)

PBMsgL2GGMCmdCancelShutupRequest = _reflection.GeneratedProtocolMessageType('PBMsgL2GGMCmdCancelShutupRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGL2GGMCMDCANCELSHUTUPREQUEST,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgL2GGMCmdCancelShutupRequest)
  ))
_sym_db.RegisterMessage(PBMsgL2GGMCmdCancelShutupRequest)

PBMsgG2SGMCmdCancelShutupNotify = _reflection.GeneratedProtocolMessageType('PBMsgG2SGMCmdCancelShutupNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2SGMCMDCANCELSHUTUPNOTIFY,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2SGMCmdCancelShutupNotify)
  ))
_sym_db.RegisterMessage(PBMsgG2SGMCmdCancelShutupNotify)

PBMsgG2DGMCmdCancelShutupNotify = _reflection.GeneratedProtocolMessageType('PBMsgG2DGMCmdCancelShutupNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2DGMCMDCANCELSHUTUPNOTIFY,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2DGMCmdCancelShutupNotify)
  ))
_sym_db.RegisterMessage(PBMsgG2DGMCmdCancelShutupNotify)

PBMsgL2GGmCmdRecoverRoleRequest = _reflection.GeneratedProtocolMessageType('PBMsgL2GGmCmdRecoverRoleRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGL2GGMCMDRECOVERROLEREQUEST,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgL2GGmCmdRecoverRoleRequest)
  ))
_sym_db.RegisterMessage(PBMsgL2GGmCmdRecoverRoleRequest)

PBMsgL2GGMCmdNoticeReq = _reflection.GeneratedProtocolMessageType('PBMsgL2GGMCmdNoticeReq', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGL2GGMCMDNOTICEREQ,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgL2GGMCmdNoticeReq)
  ))
_sym_db.RegisterMessage(PBMsgL2GGMCmdNoticeReq)

PBMsgS2GDebugCommandRequest = _reflection.GeneratedProtocolMessageType('PBMsgS2GDebugCommandRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2GDEBUGCOMMANDREQUEST,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2GDebugCommandRequest)
  ))
_sym_db.RegisterMessage(PBMsgS2GDebugCommandRequest)

PBMsgG2SChangeTimeNotify = _reflection.GeneratedProtocolMessageType('PBMsgG2SChangeTimeNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2SCHANGETIMENOTIFY,
  __module__ = 'msg_gm.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2SChangeTimeNotify)
  ))
_sym_db.RegisterMessage(PBMsgG2SChangeTimeNotify)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
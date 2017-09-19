# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_match.hxx

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import module_scene.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_match.hxx',
  package='',
  serialized_pb=_b('\n\rmsg_match.hxx\x1a\x10module_scene.hxx\"!\n\x13PBMsgS2MTestRequest\x12\n\n\x02op\x18\x01 \x01(\x05\"\"\n\x14PBMsgM2STestResponse\x12\n\n\x02op\x18\x02 \x01(\x05\"o\n\x14PBMsgG2MMatchRequest\x12\x12\n\nmatch_type\x18\x01 \x01(\x05\x12\x10\n\x08match_id\x18\x02 \x01(\x05\x12$\n\trole_data\x18\x03 \x01(\x0b\x32\x11.PBPlayerMainData\x12\x0b\n\x03mmr\x18\x04 \x01(\x05\"`\n\x15PBMsgM2GMatchResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x12\x12\n\nmatch_type\x18\x02 \x01(\x05\x12\x10\n\x08match_id\x18\x03 \x01(\x05\x12\x0f\n\x07role_id\x18\x04 \x01(\x05\"S\n\x1aPBMsgG2MMatchCancelRequest\x12\x12\n\nmatch_type\x18\x01 \x01(\x05\x12\x10\n\x08match_id\x18\x02 \x01(\x05\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\"f\n\x1bPBMsgM2GMatchCancelResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\x12\x12\n\nmatch_type\x18\x02 \x01(\x05\x12\x10\n\x08match_id\x18\x03 \x01(\x05\x12\x0f\n\x07role_id\x18\x04 \x01(\x05\"C\n\x1bPBMsgM2GCreateBattleRequest\x12$\n\trole_list\x18\x01 \x03(\x0b\x32\x11.PBPlayerMainData\"0\n\x1dPBMsgM2GClearMatchStateNotify\x12\x0f\n\x07role_id\x18\x01 \x01(\x05\"T\n PBMsgM2GSendMessageToRoleRequest\x12\x0f\n\x07role_id\x18\x01 \x01(\x05\x12\x0e\n\x06msg_id\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\x0c\x42\x02H\x01')
  ,
  dependencies=[module_scene.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBMSGS2MTESTREQUEST = _descriptor.Descriptor(
  name='PBMsgS2MTestRequest',
  full_name='PBMsgS2MTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='PBMsgS2MTestRequest.op', index=0,
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
  serialized_start=35,
  serialized_end=68,
)


_PBMSGM2STESTRESPONSE = _descriptor.Descriptor(
  name='PBMsgM2STestResponse',
  full_name='PBMsgM2STestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='PBMsgM2STestResponse.op', index=0,
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
  serialized_start=70,
  serialized_end=104,
)


_PBMSGG2MMATCHREQUEST = _descriptor.Descriptor(
  name='PBMsgG2MMatchRequest',
  full_name='PBMsgG2MMatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match_type', full_name='PBMsgG2MMatchRequest.match_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_id', full_name='PBMsgG2MMatchRequest.match_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_data', full_name='PBMsgG2MMatchRequest.role_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mmr', full_name='PBMsgG2MMatchRequest.mmr', index=3,
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
  serialized_start=106,
  serialized_end=217,
)


_PBMSGM2GMATCHRESPONSE = _descriptor.Descriptor(
  name='PBMsgM2GMatchResponse',
  full_name='PBMsgM2GMatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgM2GMatchResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_type', full_name='PBMsgM2GMatchResponse.match_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_id', full_name='PBMsgM2GMatchResponse.match_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgM2GMatchResponse.role_id', index=3,
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
  serialized_start=219,
  serialized_end=315,
)


_PBMSGG2MMATCHCANCELREQUEST = _descriptor.Descriptor(
  name='PBMsgG2MMatchCancelRequest',
  full_name='PBMsgG2MMatchCancelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match_type', full_name='PBMsgG2MMatchCancelRequest.match_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_id', full_name='PBMsgG2MMatchCancelRequest.match_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgG2MMatchCancelRequest.role_id', index=2,
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
  serialized_start=317,
  serialized_end=400,
)


_PBMSGM2GMATCHCANCELRESPONSE = _descriptor.Descriptor(
  name='PBMsgM2GMatchCancelResponse',
  full_name='PBMsgM2GMatchCancelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgM2GMatchCancelResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_type', full_name='PBMsgM2GMatchCancelResponse.match_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_id', full_name='PBMsgM2GMatchCancelResponse.match_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgM2GMatchCancelResponse.role_id', index=3,
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
  serialized_start=402,
  serialized_end=504,
)


_PBMSGM2GCREATEBATTLEREQUEST = _descriptor.Descriptor(
  name='PBMsgM2GCreateBattleRequest',
  full_name='PBMsgM2GCreateBattleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_list', full_name='PBMsgM2GCreateBattleRequest.role_list', index=0,
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
  serialized_start=506,
  serialized_end=573,
)


_PBMSGM2GCLEARMATCHSTATENOTIFY = _descriptor.Descriptor(
  name='PBMsgM2GClearMatchStateNotify',
  full_name='PBMsgM2GClearMatchStateNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgM2GClearMatchStateNotify.role_id', index=0,
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
  serialized_start=575,
  serialized_end=623,
)


_PBMSGM2GSENDMESSAGETOROLEREQUEST = _descriptor.Descriptor(
  name='PBMsgM2GSendMessageToRoleRequest',
  full_name='PBMsgM2GSendMessageToRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgM2GSendMessageToRoleRequest.role_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='PBMsgM2GSendMessageToRoleRequest.msg_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='PBMsgM2GSendMessageToRoleRequest.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=625,
  serialized_end=709,
)

_PBMSGG2MMATCHREQUEST.fields_by_name['role_data'].message_type = module_scene.hxx_pb2._PBPLAYERMAINDATA
_PBMSGM2GCREATEBATTLEREQUEST.fields_by_name['role_list'].message_type = module_scene.hxx_pb2._PBPLAYERMAINDATA
DESCRIPTOR.message_types_by_name['PBMsgS2MTestRequest'] = _PBMSGS2MTESTREQUEST
DESCRIPTOR.message_types_by_name['PBMsgM2STestResponse'] = _PBMSGM2STESTRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgG2MMatchRequest'] = _PBMSGG2MMATCHREQUEST
DESCRIPTOR.message_types_by_name['PBMsgM2GMatchResponse'] = _PBMSGM2GMATCHRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgG2MMatchCancelRequest'] = _PBMSGG2MMATCHCANCELREQUEST
DESCRIPTOR.message_types_by_name['PBMsgM2GMatchCancelResponse'] = _PBMSGM2GMATCHCANCELRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgM2GCreateBattleRequest'] = _PBMSGM2GCREATEBATTLEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgM2GClearMatchStateNotify'] = _PBMSGM2GCLEARMATCHSTATENOTIFY
DESCRIPTOR.message_types_by_name['PBMsgM2GSendMessageToRoleRequest'] = _PBMSGM2GSENDMESSAGETOROLEREQUEST

PBMsgS2MTestRequest = _reflection.GeneratedProtocolMessageType('PBMsgS2MTestRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGS2MTESTREQUEST,
  __module__ = 'msg_match.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgS2MTestRequest)
  ))
_sym_db.RegisterMessage(PBMsgS2MTestRequest)

PBMsgM2STestResponse = _reflection.GeneratedProtocolMessageType('PBMsgM2STestResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGM2STESTRESPONSE,
  __module__ = 'msg_match.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgM2STestResponse)
  ))
_sym_db.RegisterMessage(PBMsgM2STestResponse)

PBMsgG2MMatchRequest = _reflection.GeneratedProtocolMessageType('PBMsgG2MMatchRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2MMATCHREQUEST,
  __module__ = 'msg_match.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2MMatchRequest)
  ))
_sym_db.RegisterMessage(PBMsgG2MMatchRequest)

PBMsgM2GMatchResponse = _reflection.GeneratedProtocolMessageType('PBMsgM2GMatchResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGM2GMATCHRESPONSE,
  __module__ = 'msg_match.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgM2GMatchResponse)
  ))
_sym_db.RegisterMessage(PBMsgM2GMatchResponse)

PBMsgG2MMatchCancelRequest = _reflection.GeneratedProtocolMessageType('PBMsgG2MMatchCancelRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGG2MMATCHCANCELREQUEST,
  __module__ = 'msg_match.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgG2MMatchCancelRequest)
  ))
_sym_db.RegisterMessage(PBMsgG2MMatchCancelRequest)

PBMsgM2GMatchCancelResponse = _reflection.GeneratedProtocolMessageType('PBMsgM2GMatchCancelResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGM2GMATCHCANCELRESPONSE,
  __module__ = 'msg_match.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgM2GMatchCancelResponse)
  ))
_sym_db.RegisterMessage(PBMsgM2GMatchCancelResponse)

PBMsgM2GCreateBattleRequest = _reflection.GeneratedProtocolMessageType('PBMsgM2GCreateBattleRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGM2GCREATEBATTLEREQUEST,
  __module__ = 'msg_match.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgM2GCreateBattleRequest)
  ))
_sym_db.RegisterMessage(PBMsgM2GCreateBattleRequest)

PBMsgM2GClearMatchStateNotify = _reflection.GeneratedProtocolMessageType('PBMsgM2GClearMatchStateNotify', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGM2GCLEARMATCHSTATENOTIFY,
  __module__ = 'msg_match.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgM2GClearMatchStateNotify)
  ))
_sym_db.RegisterMessage(PBMsgM2GClearMatchStateNotify)

PBMsgM2GSendMessageToRoleRequest = _reflection.GeneratedProtocolMessageType('PBMsgM2GSendMessageToRoleRequest', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGM2GSENDMESSAGETOROLEREQUEST,
  __module__ = 'msg_match.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgM2GSendMessageToRoleRequest)
  ))
_sym_db.RegisterMessage(PBMsgM2GSendMessageToRoleRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
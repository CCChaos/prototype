# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: battlefield_config.hxx

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import module_fight.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='battlefield_config.hxx',
  package='',
  serialized_pb=_b('\n\x16\x62\x61ttlefield_config.hxx\x1a\x10module_fight.hxx\"0\n\x0fPBCreatureScore\x12\x0e\n\x06tpl_id\x18\x01 \x01(\x05\x12\r\n\x05score\x18\x02 \x01(\x05\"N\n\rPBPlayerScore\x12\x16\n\x0emin_multi_kill\x18\x01 \x01(\x05\x12\x16\n\x0emax_multi_kill\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x03 \x01(\x05\"Y\n\x11PBPlayerBroadcast\x12\x16\n\x0emin_multi_kill\x18\x01 \x01(\x05\x12\x16\n\x0emax_multi_kill\x18\x02 \x01(\x05\x12\x14\n\x0c\x62roadcast_id\x18\x03 \x01(\x05\";\n\x14PBCampScoreBroadcast\x12\r\n\x05score\x18\x01 \x01(\x05\x12\x14\n\x0c\x62roadcast_id\x18\x02 \x01(\x05\"w\n\x0ePBBattleReward\x12\x11\n\tmin_score\x18\x01 \x01(\x05\x12\x11\n\tmax_score\x18\x02 \x01(\x05\x12\x13\n\x0bwin_rewards\x18\x03 \x01(\t\x12\x14\n\x0c\x64raw_rewards\x18\x04 \x01(\t\x12\x14\n\x0close_rewards\x18\x05 \x01(\t\"3\n\x11PBScoreBuffBonuse\x12\x0f\n\x07\x62uff_id\x18\x01 \x01(\x05\x12\r\n\x05\x62onus\x18\x02 \x01(\x05\"\xe2\x05\n\x13PBBattlefieldConfig\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\x05\x12\x11\n\tmin_level\x18\x02 \x01(\x05\x12\x19\n\x11match_level_range\x18\x03 \x01(\x05\x12\x12\n\nmatch_time\x18\x04 \x01(\x05\x12\x1a\n\x12min_matcher_number\x18\x05 \x01(\x05\x12\x1a\n\x12max_matcher_number\x18\x06 \x01(\x05\x12\x10\n\x08scene_id\x18\x07 \x01(\x05\x12&\n\x11\x62orn_position_red\x18\x08 \x01(\x0b\x32\x0b.PBPosition\x12\'\n\x12\x62orn_position_blue\x18\t \x01(\x0b\x32\x0b.PBPosition\x12(\n\x0e\x63reature_score\x18\n \x03(\x0b\x32\x10.PBCreatureScore\x12\x31\n\x15player_kill_broadcast\x18\x0b \x03(\x0b\x32\x12.PBPlayerBroadcast\x12\x36\n\x1aplayer_be_killed_broadcast\x18\x0c \x03(\x0b\x32\x12.PBPlayerBroadcast\x12$\n\x0cplayer_score\x18\r \x03(\x0b\x32\x0e.PBPlayerScore\x12\x11\n\twin_score\x18\x0e \x01(\x05\x12.\n\x0fscore_broadcast\x18\x0f \x03(\x0b\x32\x15.PBCampScoreBroadcast\x12\x1f\n\x06reward\x18\x10 \x03(\x0b\x32\x0f.PBBattleReward\x12\x13\n\x0brace_id_red\x18\x11 \x01(\x05\x12\x14\n\x0crace_id_blue\x18\x12 \x01(\x05\x12,\n\x10score_buff_bonus\x18\x13 \x03(\x0b\x32\x12.PBScoreBuffBonuse\x12\x16\n\x0erevive_buff_id\x18\x14 \x01(\x05\x12\x18\n\x10revive_buff_time\x18\x15 \x01(\x05\x12\x16\n\x0e\x62orn_angle_red\x18\x16 \x01(\x02\x12\x17\n\x0f\x62orn_angle_blue\x18\x17 \x01(\x02\x42\x02H\x01')
  ,
  dependencies=[module_fight.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBCREATURESCORE = _descriptor.Descriptor(
  name='PBCreatureScore',
  full_name='PBCreatureScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tpl_id', full_name='PBCreatureScore.tpl_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='PBCreatureScore.score', index=1,
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
  serialized_start=44,
  serialized_end=92,
)


_PBPLAYERSCORE = _descriptor.Descriptor(
  name='PBPlayerScore',
  full_name='PBPlayerScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_multi_kill', full_name='PBPlayerScore.min_multi_kill', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_multi_kill', full_name='PBPlayerScore.max_multi_kill', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='PBPlayerScore.score', index=2,
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
  serialized_start=94,
  serialized_end=172,
)


_PBPLAYERBROADCAST = _descriptor.Descriptor(
  name='PBPlayerBroadcast',
  full_name='PBPlayerBroadcast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_multi_kill', full_name='PBPlayerBroadcast.min_multi_kill', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_multi_kill', full_name='PBPlayerBroadcast.max_multi_kill', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='broadcast_id', full_name='PBPlayerBroadcast.broadcast_id', index=2,
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
  serialized_start=174,
  serialized_end=263,
)


_PBCAMPSCOREBROADCAST = _descriptor.Descriptor(
  name='PBCampScoreBroadcast',
  full_name='PBCampScoreBroadcast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='PBCampScoreBroadcast.score', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='broadcast_id', full_name='PBCampScoreBroadcast.broadcast_id', index=1,
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
  serialized_start=265,
  serialized_end=324,
)


_PBBATTLEREWARD = _descriptor.Descriptor(
  name='PBBattleReward',
  full_name='PBBattleReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_score', full_name='PBBattleReward.min_score', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_score', full_name='PBBattleReward.max_score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='win_rewards', full_name='PBBattleReward.win_rewards', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='draw_rewards', full_name='PBBattleReward.draw_rewards', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lose_rewards', full_name='PBBattleReward.lose_rewards', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=326,
  serialized_end=445,
)


_PBSCOREBUFFBONUSE = _descriptor.Descriptor(
  name='PBScoreBuffBonuse',
  full_name='PBScoreBuffBonuse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buff_id', full_name='PBScoreBuffBonuse.buff_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bonus', full_name='PBScoreBuffBonuse.bonus', index=1,
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
  serialized_start=447,
  serialized_end=498,
)


_PBBATTLEFIELDCONFIG = _descriptor.Descriptor(
  name='PBBattlefieldConfig',
  full_name='PBBattlefieldConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_id', full_name='PBBattlefieldConfig.activity_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_level', full_name='PBBattlefieldConfig.min_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_level_range', full_name='PBBattlefieldConfig.match_level_range', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_time', full_name='PBBattlefieldConfig.match_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_matcher_number', full_name='PBBattlefieldConfig.min_matcher_number', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_matcher_number', full_name='PBBattlefieldConfig.max_matcher_number', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='PBBattlefieldConfig.scene_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='born_position_red', full_name='PBBattlefieldConfig.born_position_red', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='born_position_blue', full_name='PBBattlefieldConfig.born_position_blue', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creature_score', full_name='PBBattlefieldConfig.creature_score', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_kill_broadcast', full_name='PBBattlefieldConfig.player_kill_broadcast', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_be_killed_broadcast', full_name='PBBattlefieldConfig.player_be_killed_broadcast', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_score', full_name='PBBattlefieldConfig.player_score', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='win_score', full_name='PBBattlefieldConfig.win_score', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score_broadcast', full_name='PBBattlefieldConfig.score_broadcast', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward', full_name='PBBattlefieldConfig.reward', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='race_id_red', full_name='PBBattlefieldConfig.race_id_red', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='race_id_blue', full_name='PBBattlefieldConfig.race_id_blue', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score_buff_bonus', full_name='PBBattlefieldConfig.score_buff_bonus', index=18,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revive_buff_id', full_name='PBBattlefieldConfig.revive_buff_id', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revive_buff_time', full_name='PBBattlefieldConfig.revive_buff_time', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='born_angle_red', full_name='PBBattlefieldConfig.born_angle_red', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='born_angle_blue', full_name='PBBattlefieldConfig.born_angle_blue', index=22,
      number=23, type=2, cpp_type=6, label=1,
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
  serialized_start=501,
  serialized_end=1239,
)

_PBBATTLEFIELDCONFIG.fields_by_name['born_position_red'].message_type = module_fight.hxx_pb2._PBPOSITION
_PBBATTLEFIELDCONFIG.fields_by_name['born_position_blue'].message_type = module_fight.hxx_pb2._PBPOSITION
_PBBATTLEFIELDCONFIG.fields_by_name['creature_score'].message_type = _PBCREATURESCORE
_PBBATTLEFIELDCONFIG.fields_by_name['player_kill_broadcast'].message_type = _PBPLAYERBROADCAST
_PBBATTLEFIELDCONFIG.fields_by_name['player_be_killed_broadcast'].message_type = _PBPLAYERBROADCAST
_PBBATTLEFIELDCONFIG.fields_by_name['player_score'].message_type = _PBPLAYERSCORE
_PBBATTLEFIELDCONFIG.fields_by_name['score_broadcast'].message_type = _PBCAMPSCOREBROADCAST
_PBBATTLEFIELDCONFIG.fields_by_name['reward'].message_type = _PBBATTLEREWARD
_PBBATTLEFIELDCONFIG.fields_by_name['score_buff_bonus'].message_type = _PBSCOREBUFFBONUSE
DESCRIPTOR.message_types_by_name['PBCreatureScore'] = _PBCREATURESCORE
DESCRIPTOR.message_types_by_name['PBPlayerScore'] = _PBPLAYERSCORE
DESCRIPTOR.message_types_by_name['PBPlayerBroadcast'] = _PBPLAYERBROADCAST
DESCRIPTOR.message_types_by_name['PBCampScoreBroadcast'] = _PBCAMPSCOREBROADCAST
DESCRIPTOR.message_types_by_name['PBBattleReward'] = _PBBATTLEREWARD
DESCRIPTOR.message_types_by_name['PBScoreBuffBonuse'] = _PBSCOREBUFFBONUSE
DESCRIPTOR.message_types_by_name['PBBattlefieldConfig'] = _PBBATTLEFIELDCONFIG

PBCreatureScore = _reflection.GeneratedProtocolMessageType('PBCreatureScore', (_message.Message,), dict(
  DESCRIPTOR = _PBCREATURESCORE,
  __module__ = 'battlefield_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCreatureScore)
  ))
_sym_db.RegisterMessage(PBCreatureScore)

PBPlayerScore = _reflection.GeneratedProtocolMessageType('PBPlayerScore', (_message.Message,), dict(
  DESCRIPTOR = _PBPLAYERSCORE,
  __module__ = 'battlefield_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBPlayerScore)
  ))
_sym_db.RegisterMessage(PBPlayerScore)

PBPlayerBroadcast = _reflection.GeneratedProtocolMessageType('PBPlayerBroadcast', (_message.Message,), dict(
  DESCRIPTOR = _PBPLAYERBROADCAST,
  __module__ = 'battlefield_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBPlayerBroadcast)
  ))
_sym_db.RegisterMessage(PBPlayerBroadcast)

PBCampScoreBroadcast = _reflection.GeneratedProtocolMessageType('PBCampScoreBroadcast', (_message.Message,), dict(
  DESCRIPTOR = _PBCAMPSCOREBROADCAST,
  __module__ = 'battlefield_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBCampScoreBroadcast)
  ))
_sym_db.RegisterMessage(PBCampScoreBroadcast)

PBBattleReward = _reflection.GeneratedProtocolMessageType('PBBattleReward', (_message.Message,), dict(
  DESCRIPTOR = _PBBATTLEREWARD,
  __module__ = 'battlefield_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBBattleReward)
  ))
_sym_db.RegisterMessage(PBBattleReward)

PBScoreBuffBonuse = _reflection.GeneratedProtocolMessageType('PBScoreBuffBonuse', (_message.Message,), dict(
  DESCRIPTOR = _PBSCOREBUFFBONUSE,
  __module__ = 'battlefield_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBScoreBuffBonuse)
  ))
_sym_db.RegisterMessage(PBScoreBuffBonuse)

PBBattlefieldConfig = _reflection.GeneratedProtocolMessageType('PBBattlefieldConfig', (_message.Message,), dict(
  DESCRIPTOR = _PBBATTLEFIELDCONFIG,
  __module__ = 'battlefield_config.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBBattlefieldConfig)
  ))
_sym_db.RegisterMessage(PBBattlefieldConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_cond.hxx

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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='module_cond.hxx',
  package='',
  serialized_pb=_b('\n\x0fmodule_cond.hxx\"k\n\tPBMsgCond\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05\x12\x11\n\ttarget_id\x18\x03 \x01(\x05\x12\x0e\n\x06param1\x18\x04 \x01(\x05\x12\x0e\n\x06param2\x18\x05 \x01(\x05\x12\x0e\n\x06param3\x18\x06 \x01(\x05\")\n\rPBMsgCondList\x12\x18\n\x04\x63ond\x18\x01 \x03(\x0b\x32\n.PBMsgCond*\xc3\x16\n\tECondType\x12\x18\n\x14TASK_CHECKER_INVALID\x10\x00\x12\x13\n\x0fROLE_LV_CHECKER\x10\x01\x12\x18\n\x14KILL_MONSTER_CHECKER\x10\x02\x12\x12\n\x0eGATHER_CHECKER\x10\x03\x12\x14\n\x10PRE_TASK_CHECKER\x10\x04\x12\x19\n\x15\x43OND_TYPE_MAX_ROLE_LV\x10\x05\x12\x16\n\x12ROLE_OCCUP_CHECKER\x10\x06\x12\x17\n\x13ROLE_GENDER_CHECKER\x10\x07\x12\x14\n\x10OWN_PROP_CHECKER\x10\x08\x12\x14\n\x10USE_PROP_CHECKER\x10\t\x12\x16\n\x12\x43OND_TYPE_POSITION\x10\n\x12\x16\n\x12PLAY_DRAMA_CHECKER\x10\x0b\x12\x1c\n\x18\x43OMPLETE_DUNGEON_CHECKER\x10\x0c\x12\x19\n\x15\x41\x43\x43\x45PTED_TASK_CHECKER\x10\r\x12\x1d\n\x19SUB_TASK_PROGRESS_CHECKER\x10\x0e\x12\x18\n\x14\x43OND_TYPE_PET_MIN_LV\x10\x0f\x12\x1a\n\x16\x43OND_TYPE_PET_MIN_DUAN\x10\x10\x12\x1f\n\x1b\x43OND_TYPE_COMPLETE_ACTIVITY\x10\x11\x12\x19\n\x15\x43OND_TYPE_PET_MIN_JIE\x10\x12\x12\x1e\n\x1a\x43OND_TYPE_PET_COMBAT_POWER\x10\x13\x12\x1b\n\x17\x43OND_TYPE_HAND_IN_PROPS\x10\x14\x12\x1b\n\x17\x43OND_TYPE_HAND_IN_EQUIP\x10\x15\x12\x1d\n\x19\x43OND_TYPE_EQUIP_SHENGXING\x10\x16\x12\x1b\n\x17\x43OND_TYPE_EQUIP_LIANHUA\x10\x17\x12\x1a\n\x16\x43OND_TYPE_EQUIP_XILIAN\x10\x18\x12\x1c\n\x18\x43OND_TYPE_EQUIP_QIANGHUA\x10\x19\x12\x1c\n\x18\x43OND_TYPE_EQUIP_JIANDING\x10\x1a\x12\x1a\n\x16\x43OND_TYPE_EQUIP_JUANKE\x10\x1b\x12\x17\n\x13\x43OND_TYPE_GEM_INLAY\x10\x1c\x12\x19\n\x15\x43OND_TYPE_GEM_HECHENG\x10\x1d\x12\x1d\n\x19\x43OND_TYPE_PET_TRAIN_ZIZHI\x10\x1e\x12\x1e\n\x1a\x43OND_TYPE_PET_TRAIN_GROWTH\x10\x1f\x12\x1d\n\x19\x43OND_TYPE_PET_LEARN_SKILL\x10 \x12\x1f\n\x1b\x43OND_TYPE_PET_UPGRADE_SKILL\x10!\x12\x1a\n\x16\x43OND_TYPE_GUILD_DONATE\x10\"\x12\x18\n\x14\x43OND_TYPE_GUILD_JOIN\x10#\x12\x18\n\x14\x43OND_TYPE_FRIEND_ADD\x10$\x12\x17\n\x13\x43OND_TYPE_CAMP_JOIN\x10%\x12\x1c\n\x18\x43OND_TYPE_SKILL_LEVEL_UP\x10&\x12\x13\n\x0f\x43OND_TYPE_POWER\x10\'\x12$\n COND_TYPE_EQUIP_JUANKE_RESONANCE\x10(\x12!\n\x1d\x43OND_TYPE_GEM_RESONANCE_LEVEL\x10)\x12$\n COND_TYPE_EQUIP_MULTI_ATTR_COUNT\x10*\x12\x1d\n\x19\x43OND_TYPE_PET_SKILL_COUNT\x10+\x12\x1f\n\x1b\x43OND_TYPE_PET_HUANHUA_COUNT\x10,\x12\x1b\n\x17\x43OND_TYPE_PET_ZIZHI_SUM\x10-\x12*\n&COND_TYPE_TASK_COMMITTED_COUNT_BY_TYPE\x10.\x12%\n!COND_TYPE_SKILL_GUILD_LEVEL_COUNT\x10/\x12\x1e\n\x1a\x43OND_TYPE_KILL_MONSTER_ANY\x10\x30\x12\x1f\n\x1b\x43OND_TYPE_ACHIEVEMENT_POINT\x10\x31\x12\x1e\n\x1a\x43OND_TYPE_EQUIP_PART_CLASS\x10\x32\x12,\n(COND_TYPE_EQUIP_QIANGHUA_RESONANCE_LEVEL\x10\x33\x12)\n%COND_TYPE_EQUIP_PERFECT_QIANHUA_COUNT\x10\x34\x12\x1d\n\x19\x43OND_TYPE_PET_SKILL_LEVEL\x10\x35\x12\x1c\n\x18\x43OND_TYPE_PET_SKIN_COUNT\x10\x36\x12\x16\n\x12\x43OND_TYPE_PET_SKIN\x10\x37\x12\x1d\n\x19\x43OND_TYPE_SKILL_ANY_LEVEL\x10\x38\x12%\n!COND_TYPE_SKILL_INSCRIPTION_COUNT\x10\x39\x12\x19\n\x15\x43OND_TYPE_MOUNT_COUNT\x10:\x12\x18\n\x14\x43OND_TYPE_MOUNT_SPEC\x10;\x12\x1d\n\x19\x43OND_TYPE_ACHEVEMENT_SPEC\x10<\x12%\n!COND_TYPE_FASHION_NON_TIMED_COUNT\x10=\x12\x12\n\x0e\x43OND_TYPE_SIGN\x10>\x12\x18\n\x14\x43OND_TYPE_RANK_FIRST\x10?\x12)\n%COND_TYPE_COMPLETE_INSTANCE_SPEC_TYPE\x10@\x12&\n\"COND_TYPE_TXFM_KILL_BOSS_SPEC_TYPE\x10\x41\x12%\n!COND_TYPE_TXFM_LAST_HIT_SPEC_TYPE\x10\x42\x12,\n(COND_TYPE_CAPTAIN_COMPLETE_TEAM_INSTANCE\x10\x43\x12\x1f\n\x1b\x43OND_TYPE_COMMIT_TASK_TIMES\x10\x44\x12!\n\x1d\x43OND_TYPE_ACTIVITY_RANK_TIMES\x10\x45\x12!\n\x1d\x43OND_TYPE_GUILD_WAR_WIN_COUNT\x10\x46\x12 \n\x1c\x43OND_TYPE_SEND_FLOWERS_COUNT\x10G\x12#\n\x1f\x43OND_TYPE_RECEIVE_FLOWERS_COUNT\x10H\x12\x1c\n\x18\x43OND_TYPE_BABY_SPEC_TYPE\x10I\x12\x1c\n\x18\x43OND_TYPE_KILL_CAMP_ROLE\x10J\x12\x1c\n\x18\x43OND_TYPE_WILD_DIE_TIMES\x10K\x12\x1b\n\x17\x43OND_TYPE_SKILL_UPGRADE\x10L\x12\x1b\n\x17\x43OND_TYPE_NUMERICAL_SUM\x10M\x12\x1b\n\x17\x43OND_TYPE_JOIN_ACTIVITY\x10N\x12\x17\n\x13\x43OND_TYPE_DALUANDOU\x10O\x12\x14\n\x10\x43OND_TYPE_BATTLE\x10P\x12\x1a\n\x16\x43OND_TYPE_ROLESKILL_LV\x10Q\x12\x19\n\x15\x43OND_TYPE_HAND_IN_ONE\x10R\x12 \n\x1c\x43OND_TYPE_KILL_MONSTER_YEWAI\x10S\x12\x1c\n\x18\x43OND_TYPE_QIANGHUA_COUNT\x10T\x12\x1a\n\x16\x43OND_TYPE_JINJIE_COUNT\x10U\x12\x1d\n\x19\x43OND_TYPE_GEM_INLAY_COUNT\x10V\x12 \n\x1c\x43OND_TYPE_EQUIP_XILIAN_COUNT\x10W\x12!\n\x1d\x43OND_TYPE_EQUIP_ENGRAVE_COUNT\x10X\x12\x18\n\x14\x43OND_TYPE_GUILD_TASK\x10Y\x12\x1f\n\x1b\x43OND_TYPE_LEARN_GUILD_SKILL\x10Z\x12\x1f\n\x1b\x43OND_TYPE_GUILD_SKILL_COUNT\x10[\x12\x16\n\x12\x43OND_TYPE_HUOYUEDU\x10\\\x12&\n\"COND_TYPE_EQUIP_XILIAN_TOTAL_COUNT\x10]\x12\x12\n\rCOND_TYPE_MAX\x10\xe7\x07\x42\x02H\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ECONDTYPE = _descriptor.EnumDescriptor(
  name='ECondType',
  full_name='ECondType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TASK_CHECKER_INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROLE_LV_CHECKER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILL_MONSTER_CHECKER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GATHER_CHECKER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_TASK_CHECKER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_MAX_ROLE_LV', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROLE_OCCUP_CHECKER', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROLE_GENDER_CHECKER', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OWN_PROP_CHECKER', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_PROP_CHECKER', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_POSITION', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAY_DRAMA_CHECKER', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE_DUNGEON_CHECKER', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCEPTED_TASK_CHECKER', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUB_TASK_PROGRESS_CHECKER', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_MIN_LV', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_MIN_DUAN', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_COMPLETE_ACTIVITY', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_MIN_JIE', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_COMBAT_POWER', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_HAND_IN_PROPS', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_HAND_IN_EQUIP', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_SHENGXING', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_LIANHUA', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_XILIAN', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_QIANGHUA', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_JIANDING', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_JUANKE', index=27, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_GEM_INLAY', index=28, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_GEM_HECHENG', index=29, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_TRAIN_ZIZHI', index=30, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_TRAIN_GROWTH', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_LEARN_SKILL', index=32, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_UPGRADE_SKILL', index=33, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_GUILD_DONATE', index=34, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_GUILD_JOIN', index=35, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_FRIEND_ADD', index=36, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_CAMP_JOIN', index=37, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_SKILL_LEVEL_UP', index=38, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_POWER', index=39, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_JUANKE_RESONANCE', index=40, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_GEM_RESONANCE_LEVEL', index=41, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_MULTI_ATTR_COUNT', index=42, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_SKILL_COUNT', index=43, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_HUANHUA_COUNT', index=44, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_ZIZHI_SUM', index=45, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_TASK_COMMITTED_COUNT_BY_TYPE', index=46, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_SKILL_GUILD_LEVEL_COUNT', index=47, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_KILL_MONSTER_ANY', index=48, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_ACHIEVEMENT_POINT', index=49, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_PART_CLASS', index=50, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_QIANGHUA_RESONANCE_LEVEL', index=51, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_PERFECT_QIANHUA_COUNT', index=52, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_SKILL_LEVEL', index=53, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_SKIN_COUNT', index=54, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_PET_SKIN', index=55, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_SKILL_ANY_LEVEL', index=56, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_SKILL_INSCRIPTION_COUNT', index=57, number=57,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_MOUNT_COUNT', index=58, number=58,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_MOUNT_SPEC', index=59, number=59,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_ACHEVEMENT_SPEC', index=60, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_FASHION_NON_TIMED_COUNT', index=61, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_SIGN', index=62, number=62,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_RANK_FIRST', index=63, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_COMPLETE_INSTANCE_SPEC_TYPE', index=64, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_TXFM_KILL_BOSS_SPEC_TYPE', index=65, number=65,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_TXFM_LAST_HIT_SPEC_TYPE', index=66, number=66,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_CAPTAIN_COMPLETE_TEAM_INSTANCE', index=67, number=67,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_COMMIT_TASK_TIMES', index=68, number=68,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_ACTIVITY_RANK_TIMES', index=69, number=69,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_GUILD_WAR_WIN_COUNT', index=70, number=70,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_SEND_FLOWERS_COUNT', index=71, number=71,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_RECEIVE_FLOWERS_COUNT', index=72, number=72,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_BABY_SPEC_TYPE', index=73, number=73,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_KILL_CAMP_ROLE', index=74, number=74,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_WILD_DIE_TIMES', index=75, number=75,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_SKILL_UPGRADE', index=76, number=76,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_NUMERICAL_SUM', index=77, number=77,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_JOIN_ACTIVITY', index=78, number=78,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_DALUANDOU', index=79, number=79,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_BATTLE', index=80, number=80,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_ROLESKILL_LV', index=81, number=81,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_HAND_IN_ONE', index=82, number=82,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_KILL_MONSTER_YEWAI', index=83, number=83,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_QIANGHUA_COUNT', index=84, number=84,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_JINJIE_COUNT', index=85, number=85,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_GEM_INLAY_COUNT', index=86, number=86,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_XILIAN_COUNT', index=87, number=87,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_ENGRAVE_COUNT', index=88, number=88,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_GUILD_TASK', index=89, number=89,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_LEARN_GUILD_SKILL', index=90, number=90,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_GUILD_SKILL_COUNT', index=91, number=91,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_HUOYUEDU', index=92, number=92,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_EQUIP_XILIAN_TOTAL_COUNT', index=93, number=93,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COND_TYPE_MAX', index=94, number=999,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=172,
  serialized_end=3055,
)
_sym_db.RegisterEnumDescriptor(_ECONDTYPE)

ECondType = enum_type_wrapper.EnumTypeWrapper(_ECONDTYPE)
TASK_CHECKER_INVALID = 0
ROLE_LV_CHECKER = 1
KILL_MONSTER_CHECKER = 2
GATHER_CHECKER = 3
PRE_TASK_CHECKER = 4
COND_TYPE_MAX_ROLE_LV = 5
ROLE_OCCUP_CHECKER = 6
ROLE_GENDER_CHECKER = 7
OWN_PROP_CHECKER = 8
USE_PROP_CHECKER = 9
COND_TYPE_POSITION = 10
PLAY_DRAMA_CHECKER = 11
COMPLETE_DUNGEON_CHECKER = 12
ACCEPTED_TASK_CHECKER = 13
SUB_TASK_PROGRESS_CHECKER = 14
COND_TYPE_PET_MIN_LV = 15
COND_TYPE_PET_MIN_DUAN = 16
COND_TYPE_COMPLETE_ACTIVITY = 17
COND_TYPE_PET_MIN_JIE = 18
COND_TYPE_PET_COMBAT_POWER = 19
COND_TYPE_HAND_IN_PROPS = 20
COND_TYPE_HAND_IN_EQUIP = 21
COND_TYPE_EQUIP_SHENGXING = 22
COND_TYPE_EQUIP_LIANHUA = 23
COND_TYPE_EQUIP_XILIAN = 24
COND_TYPE_EQUIP_QIANGHUA = 25
COND_TYPE_EQUIP_JIANDING = 26
COND_TYPE_EQUIP_JUANKE = 27
COND_TYPE_GEM_INLAY = 28
COND_TYPE_GEM_HECHENG = 29
COND_TYPE_PET_TRAIN_ZIZHI = 30
COND_TYPE_PET_TRAIN_GROWTH = 31
COND_TYPE_PET_LEARN_SKILL = 32
COND_TYPE_PET_UPGRADE_SKILL = 33
COND_TYPE_GUILD_DONATE = 34
COND_TYPE_GUILD_JOIN = 35
COND_TYPE_FRIEND_ADD = 36
COND_TYPE_CAMP_JOIN = 37
COND_TYPE_SKILL_LEVEL_UP = 38
COND_TYPE_POWER = 39
COND_TYPE_EQUIP_JUANKE_RESONANCE = 40
COND_TYPE_GEM_RESONANCE_LEVEL = 41
COND_TYPE_EQUIP_MULTI_ATTR_COUNT = 42
COND_TYPE_PET_SKILL_COUNT = 43
COND_TYPE_PET_HUANHUA_COUNT = 44
COND_TYPE_PET_ZIZHI_SUM = 45
COND_TYPE_TASK_COMMITTED_COUNT_BY_TYPE = 46
COND_TYPE_SKILL_GUILD_LEVEL_COUNT = 47
COND_TYPE_KILL_MONSTER_ANY = 48
COND_TYPE_ACHIEVEMENT_POINT = 49
COND_TYPE_EQUIP_PART_CLASS = 50
COND_TYPE_EQUIP_QIANGHUA_RESONANCE_LEVEL = 51
COND_TYPE_EQUIP_PERFECT_QIANHUA_COUNT = 52
COND_TYPE_PET_SKILL_LEVEL = 53
COND_TYPE_PET_SKIN_COUNT = 54
COND_TYPE_PET_SKIN = 55
COND_TYPE_SKILL_ANY_LEVEL = 56
COND_TYPE_SKILL_INSCRIPTION_COUNT = 57
COND_TYPE_MOUNT_COUNT = 58
COND_TYPE_MOUNT_SPEC = 59
COND_TYPE_ACHEVEMENT_SPEC = 60
COND_TYPE_FASHION_NON_TIMED_COUNT = 61
COND_TYPE_SIGN = 62
COND_TYPE_RANK_FIRST = 63
COND_TYPE_COMPLETE_INSTANCE_SPEC_TYPE = 64
COND_TYPE_TXFM_KILL_BOSS_SPEC_TYPE = 65
COND_TYPE_TXFM_LAST_HIT_SPEC_TYPE = 66
COND_TYPE_CAPTAIN_COMPLETE_TEAM_INSTANCE = 67
COND_TYPE_COMMIT_TASK_TIMES = 68
COND_TYPE_ACTIVITY_RANK_TIMES = 69
COND_TYPE_GUILD_WAR_WIN_COUNT = 70
COND_TYPE_SEND_FLOWERS_COUNT = 71
COND_TYPE_RECEIVE_FLOWERS_COUNT = 72
COND_TYPE_BABY_SPEC_TYPE = 73
COND_TYPE_KILL_CAMP_ROLE = 74
COND_TYPE_WILD_DIE_TIMES = 75
COND_TYPE_SKILL_UPGRADE = 76
COND_TYPE_NUMERICAL_SUM = 77
COND_TYPE_JOIN_ACTIVITY = 78
COND_TYPE_DALUANDOU = 79
COND_TYPE_BATTLE = 80
COND_TYPE_ROLESKILL_LV = 81
COND_TYPE_HAND_IN_ONE = 82
COND_TYPE_KILL_MONSTER_YEWAI = 83
COND_TYPE_QIANGHUA_COUNT = 84
COND_TYPE_JINJIE_COUNT = 85
COND_TYPE_GEM_INLAY_COUNT = 86
COND_TYPE_EQUIP_XILIAN_COUNT = 87
COND_TYPE_EQUIP_ENGRAVE_COUNT = 88
COND_TYPE_GUILD_TASK = 89
COND_TYPE_LEARN_GUILD_SKILL = 90
COND_TYPE_GUILD_SKILL_COUNT = 91
COND_TYPE_HUOYUEDU = 92
COND_TYPE_EQUIP_XILIAN_TOTAL_COUNT = 93
COND_TYPE_MAX = 999



_PBMSGCOND = _descriptor.Descriptor(
  name='PBMsgCond',
  full_name='PBMsgCond',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='PBMsgCond.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PBMsgCond.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='PBMsgCond.target_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param1', full_name='PBMsgCond.param1', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param2', full_name='PBMsgCond.param2', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param3', full_name='PBMsgCond.param3', index=5,
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
  serialized_start=19,
  serialized_end=126,
)


_PBMSGCONDLIST = _descriptor.Descriptor(
  name='PBMsgCondList',
  full_name='PBMsgCondList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cond', full_name='PBMsgCondList.cond', index=0,
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
  serialized_start=128,
  serialized_end=169,
)

_PBMSGCONDLIST.fields_by_name['cond'].message_type = _PBMSGCOND
DESCRIPTOR.message_types_by_name['PBMsgCond'] = _PBMSGCOND
DESCRIPTOR.message_types_by_name['PBMsgCondList'] = _PBMSGCONDLIST
DESCRIPTOR.enum_types_by_name['ECondType'] = _ECONDTYPE

PBMsgCond = _reflection.GeneratedProtocolMessageType('PBMsgCond', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGCOND,
  __module__ = 'module_cond.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgCond)
  ))
_sym_db.RegisterMessage(PBMsgCond)

PBMsgCondList = _reflection.GeneratedProtocolMessageType('PBMsgCondList', (_message.Message,), dict(
  DESCRIPTOR = _PBMSGCONDLIST,
  __module__ = 'module_cond.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBMsgCondList)
  ))
_sym_db.RegisterMessage(PBMsgCondList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
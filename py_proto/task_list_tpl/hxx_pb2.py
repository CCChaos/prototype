# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_list_tpl.hxx

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import module_task.hxx_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task_list_tpl.hxx',
  package='',
  serialized_pb=_b('\n\x11task_list_tpl.hxx\x1a\x0fmodule_task.hxx\"4\n\x11PBTplTaskListItem\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\x0e\n\x06weight\x18\x02 \x01(\x05\"e\n\rPBTplTaskList\x12\n\n\x02id\x18\x01 \x01(\x05\x12&\n\x0etask_list_type\x18\x02 \x01(\x0e\x32\x0e.ETaskListType\x12 \n\x04task\x18\x03 \x03(\x0b\x32\x12.PBTplTaskListItemB\x02H\x01')
  ,
  dependencies=[module_task.hxx_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBTPLTASKLISTITEM = _descriptor.Descriptor(
  name='PBTplTaskListItem',
  full_name='PBTplTaskListItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='PBTplTaskListItem.task_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight', full_name='PBTplTaskListItem.weight', index=1,
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
  serialized_start=38,
  serialized_end=90,
)


_PBTPLTASKLIST = _descriptor.Descriptor(
  name='PBTplTaskList',
  full_name='PBTplTaskList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PBTplTaskList.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_list_type', full_name='PBTplTaskList.task_list_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task', full_name='PBTplTaskList.task', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=92,
  serialized_end=193,
)

_PBTPLTASKLIST.fields_by_name['task_list_type'].enum_type = module_task.hxx_pb2._ETASKLISTTYPE
_PBTPLTASKLIST.fields_by_name['task'].message_type = _PBTPLTASKLISTITEM
DESCRIPTOR.message_types_by_name['PBTplTaskListItem'] = _PBTPLTASKLISTITEM
DESCRIPTOR.message_types_by_name['PBTplTaskList'] = _PBTPLTASKLIST

PBTplTaskListItem = _reflection.GeneratedProtocolMessageType('PBTplTaskListItem', (_message.Message,), dict(
  DESCRIPTOR = _PBTPLTASKLISTITEM,
  __module__ = 'task_list_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBTplTaskListItem)
  ))
_sym_db.RegisterMessage(PBTplTaskListItem)

PBTplTaskList = _reflection.GeneratedProtocolMessageType('PBTplTaskList', (_message.Message,), dict(
  DESCRIPTOR = _PBTPLTASKLIST,
  __module__ = 'task_list_tpl.hxx_pb2'
  # @@protoc_insertion_point(class_scope:PBTplTaskList)
  ))
_sym_db.RegisterMessage(PBTplTaskList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)

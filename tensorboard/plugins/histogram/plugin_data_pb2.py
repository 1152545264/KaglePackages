# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/plugins/histogram/plugin_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/plugins/histogram/plugin_data.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/tensorboard/plugins/histogram/plugin_data.proto\x12\x0btensorboard\"&\n\x13HistogramPluginData\x12\x0f\n\x07version\x18\x01 \x01(\x05\x62\x06proto3')
)




_HISTOGRAMPLUGINDATA = _descriptor.Descriptor(
  name='HistogramPluginData',
  full_name='tensorboard.HistogramPluginData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorboard.HistogramPluginData.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['HistogramPluginData'] = _HISTOGRAMPLUGINDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HistogramPluginData = _reflection.GeneratedProtocolMessageType('HistogramPluginData', (_message.Message,), {
  'DESCRIPTOR' : _HISTOGRAMPLUGINDATA,
  '__module__' : 'tensorboard.plugins.histogram.plugin_data_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.HistogramPluginData)
  })
_sym_db.RegisterMessage(HistogramPluginData)


# @@protoc_insertion_point(module_scope)

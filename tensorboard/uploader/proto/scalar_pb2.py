# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/uploader/proto/scalar.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tensorboard.compat.proto import summary_pb2 as tensorboard_dot_compat_dot_proto_dot_summary__pb2
try:
  tensorboard_dot_compat_dot_proto_dot_histogram__pb2 = tensorboard_dot_compat_dot_proto_dot_summary__pb2.tensorboard_dot_compat_dot_proto_dot_histogram__pb2
except AttributeError:
  tensorboard_dot_compat_dot_proto_dot_histogram__pb2 = tensorboard_dot_compat_dot_proto_dot_summary__pb2.tensorboard.compat.proto.histogram_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/uploader/proto/scalar.proto',
  package='tensorboard.service',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'tensorboard/uploader/proto/scalar.proto\x12\x13tensorboard.service\x1a\x1fgoogle/protobuf/timestamp.proto\x1a&tensorboard/compat/proto/summary.proto\"Y\n\x0bScalarPoint\x12\x0c\n\x04step\x18\x01 \x01(\x03\x12-\n\twall_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05value\x18\x03 \x01(\x01\"\x92\x01\n\x13ScalarPointMetadata\x12\x10\n\x08max_step\x18\x01 \x01(\x03\x12\x31\n\rmax_wall_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10summary_metadata\x18\x03 \x01(\x0b\x32\x1c.tensorboard.SummaryMetadatab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,tensorboard_dot_compat_dot_proto_dot_summary__pb2.DESCRIPTOR,])




_SCALARPOINT = _descriptor.Descriptor(
  name='ScalarPoint',
  full_name='tensorboard.service.ScalarPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='tensorboard.service.ScalarPoint.step', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wall_time', full_name='tensorboard.service.ScalarPoint.wall_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.service.ScalarPoint.value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=137,
  serialized_end=226,
)


_SCALARPOINTMETADATA = _descriptor.Descriptor(
  name='ScalarPointMetadata',
  full_name='tensorboard.service.ScalarPointMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_step', full_name='tensorboard.service.ScalarPointMetadata.max_step', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_wall_time', full_name='tensorboard.service.ScalarPointMetadata.max_wall_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary_metadata', full_name='tensorboard.service.ScalarPointMetadata.summary_metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=229,
  serialized_end=375,
)

_SCALARPOINT.fields_by_name['wall_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SCALARPOINTMETADATA.fields_by_name['max_wall_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SCALARPOINTMETADATA.fields_by_name['summary_metadata'].message_type = tensorboard_dot_compat_dot_proto_dot_summary__pb2._SUMMARYMETADATA
DESCRIPTOR.message_types_by_name['ScalarPoint'] = _SCALARPOINT
DESCRIPTOR.message_types_by_name['ScalarPointMetadata'] = _SCALARPOINTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScalarPoint = _reflection.GeneratedProtocolMessageType('ScalarPoint', (_message.Message,), {
  'DESCRIPTOR' : _SCALARPOINT,
  '__module__' : 'tensorboard.uploader.proto.scalar_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.ScalarPoint)
  })
_sym_db.RegisterMessage(ScalarPoint)

ScalarPointMetadata = _reflection.GeneratedProtocolMessageType('ScalarPointMetadata', (_message.Message,), {
  'DESCRIPTOR' : _SCALARPOINTMETADATA,
  '__module__' : 'tensorboard.uploader.proto.scalar_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.ScalarPointMetadata)
  })
_sym_db.RegisterMessage(ScalarPointMetadata)


# @@protoc_insertion_point(module_scope)
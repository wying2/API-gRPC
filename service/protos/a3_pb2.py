# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/a3.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fprotos/a3.proto\x12\x06protos\"\xb4\x01\n\x04\x42ook\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12!\n\x05genre\x18\x04 \x01(\x0e\x32\x12.protos.Book.Genre\x12\x13\n\x0bpublishYear\x18\x05 \x01(\x05\"G\n\x05Genre\x12\x0b\n\x07\x46ICTION\x10\x00\x12\r\n\tBIOGRAPHY\x10\x01\x12\x07\n\x03\x41RT\x10\x02\x12\x0b\n\x07SCIENCE\x10\x03\x12\x0c\n\x08\x42usiness\x10\x04\"\x9b\x01\n\rInventoryItem\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12,\n\x06status\x18\x02 \x01(\x0e\x32\x1c.protos.InventoryItem.Status\x12\x1c\n\x04\x42ook\x18\x03 \x01(\x0b\x32\x0c.protos.BookH\x00\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x42\n\n\x08itemTypeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.a3_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=28
  _BOOK._serialized_end=208
  _BOOK_GENRE._serialized_start=137
  _BOOK_GENRE._serialized_end=208
  _INVENTORYITEM._serialized_start=211
  _INVENTORYITEM._serialized_end=366
  _INVENTORYITEM_STATUS._serialized_start=320
  _INVENTORYITEM_STATUS._serialized_end=354
# @@protoc_insertion_point(module_scope)

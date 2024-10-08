# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13order_service.proto\x12\rorder_service\"L\n\x0cOrderRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\'\n\x05items\x18\x02 \x03(\x0b\x32\x18.order_service.OrderItem\"\x83\x01\n\rOrderResponse\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ustomer_id\x18\x02 \x01(\t\x12\'\n\x05items\x18\x03 \x03(\x0b\x32\x18.order_service.OrderItem\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\t\"\x1b\n\x07OrderID\x12\x10\n\x08order_id\x18\x01 \x01(\t\"9\n\tOrderList\x12,\n\x06orders\x18\x01 \x03(\x0b\x32\x1c.order_service.OrderResponse\"1\n\tOrderItem\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"\x07\n\x05\x45mpty2\xd8\x01\n\x0cOrderService\x12H\n\x0b\x43reateOrder\x12\x1b.order_service.OrderRequest\x1a\x1c.order_service.OrderResponse\x12@\n\x08GetOrder\x12\x16.order_service.OrderID\x1a\x1c.order_service.OrderResponse\x12<\n\nListOrders\x12\x14.order_service.Empty\x1a\x18.order_service.OrderListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'order_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ORDERREQUEST']._serialized_start=38
  _globals['_ORDERREQUEST']._serialized_end=114
  _globals['_ORDERRESPONSE']._serialized_start=117
  _globals['_ORDERRESPONSE']._serialized_end=248
  _globals['_ORDERID']._serialized_start=250
  _globals['_ORDERID']._serialized_end=277
  _globals['_ORDERLIST']._serialized_start=279
  _globals['_ORDERLIST']._serialized_end=336
  _globals['_ORDERITEM']._serialized_start=338
  _globals['_ORDERITEM']._serialized_end=387
  _globals['_EMPTY']._serialized_start=389
  _globals['_EMPTY']._serialized_end=396
  _globals['_ORDERSERVICE']._serialized_start=399
  _globals['_ORDERSERVICE']._serialized_end=615
# @@protoc_insertion_point(module_scope)

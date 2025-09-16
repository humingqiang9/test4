#!/usr/bin/env python3

import sys
import glob
sys.path.append('gen-py')

from order_service import OrderProcessor
from order_service.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class OrderHandler:
    def __init__(self):
        self.orders = {}
        self.next_order_id = 1

    def createOrder(self, request):
        print(f"Creating order for {request.customer_name}")
        order = Order(
            id=self.next_order_id,
            customer_name=request.customer_name,
            items=request.items,
            total_amount=request.total_amount,
            status="CREATED"
        )
        self.orders[self.next_order_id] = order
        response = OrderResponse(
            success=True,
            message=f"Order {self.next_order_id} created successfully",
            order_id=self.next_order_id
        )
        self.next_order_id += 1
        return response

    def getOrder(self, order_id):
        print(f"Retrieving order {order_id}")
        if order_id in self.orders:
            return self.orders[order_id]
        else:
            raise OrderException(message=f"Order {order_id} not found")

    def updateOrderStatus(self, order_id, status):
        print(f"Updating order {order_id} status to {status}")
        if order_id in self.orders:
            self.orders[order_id].status = status
            return True
        else:
            raise OrderException(message=f"Order {order_id} not found")
    
    def listOrders(self):
        print("Listing all orders")
        return list(self.orders.values())

if __name__ == '__main__':
    handler = OrderHandler()
    processor = OrderProcessor.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    
    print("Starting the order service server...")
    server.serve()
#!/usr/bin/env python3

import sys
sys.path.append('gen-py')

from order_service import OrderProcessor
from order_service.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
    # Создаем соединение с сервером
    transport = TSocket.TSocket('127.0.0.1', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = OrderProcessor.Client(protocol)
    
    # Открываем соединение
    transport.open()
    
    try:
        # Создаем заказ
        request = OrderRequest(
            customer_name="John Doe",
            items="Product A, Product B",
            total_amount=29.99
        )
        response = client.createOrder(request)
        print(f"Create order response: {response.message}")
        
        # Получаем заказ
        order = client.getOrder(response.order_id)
        print(f"Retrieved order: {order}")
        
        # Обновляем статус заказа
        success = client.updateOrderStatus(response.order_id, "SHIPPED")
        print(f"Update status success: {success}")
        
        # Получаем обновленный заказ
        updated_order = client.getOrder(response.order_id)
        print(f"Updated order: {updated_order}")
        
        # Создаем еще один заказ
        request2 = OrderRequest(
            customer_name="Jane Smith",
            items="Product C",
            total_amount=15.50
        )
        response2 = client.createOrder(request2)
        print(f"Create order 2 response: {response2.message}")
        
        # Получаем список всех заказов
        orders = client.listOrders()
        print("All orders:")
        for o in orders:
            print(f"  Order {o.id}: {o.customer_name} - {o.status}")
            
    except OrderException as e:
        print(f"Order exception: {e.message}")
    except Thrift.TException as tx:
        print(f"Thrift exception: {tx.message}")
    finally:
        # Закрываем соединение
        transport.close()

if __name__ == '__main__':
    main()
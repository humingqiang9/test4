# Thrift Order Processing Service

This service provides functionality for processing orders in an e-commerce system.

## Service Definition

The service is defined in the `order_service.thrift` file which includes:

- Data structures for orders and order items
- Enum for order status tracking
- Exception definition for error handling
- Service interface with methods for order management

## Usage

To generate code from the Thrift IDL file, use the Thrift compiler:

```bash
thrift -r --gen <language> order_service.thrift
```

Replace `<language>` with your target language (e.g., java, py, cpp).

## Service Methods

1. `createOrder` - Creates a new order and returns the order ID
2. `getOrder` - Retrieves order details by order ID
3. `updateOrderStatus` - Updates the status of an existing order
4. `cancelOrder` - Cancels an order
5. `getOrdersByCustomer` - Retrieves all orders for a specific customer

## Data Structures

- `Order`: Main order structure containing all order details
- `OrderItem`: Individual items within an order
- `OrderStatus`: Enumeration of possible order statuses
- `OrderException`: Exception thrown for order-related errors
namespace py order_service

struct Order {
    1: i32 id,
    2: string customer_name,
    3: string items,
    4: double total_amount,
    5: string status
}

struct OrderRequest {
    1: string customer_name,
    2: string items,
    3: double total_amount
}

struct OrderResponse {
    1: bool success,
    2: string message,
    3: i32 order_id
}

exception OrderException {
    1: string message
}

service OrderProcessor {
    OrderResponse createOrder(1: OrderRequest request) throws (1: OrderException ex),
    Order getOrder(1: i32 order_id) throws (1: OrderException ex),
    bool updateOrderStatus(1: i32 order_id, 2: string status) throws (1: OrderException ex),
    list<Order> listOrders()
}
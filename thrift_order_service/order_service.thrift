namespace java com.example.order
namespace py order_service

// Статус заказа
enum OrderStatus {
  CREATED = 1,
  PAID = 2,
  SHIPPED = 3,
  DELIVERED = 4,
  CANCELLED = 5
}

// Структура элемента заказа
struct OrderItem {
  1: string productId,
  2: i32 quantity,
  3: double price
}

// Структура заказа
struct Order {
  1: string orderId,
  2: string customerId,
  3: list<OrderItem> items,
  4: double totalAmount,
  5: OrderStatus status,
  6: i64 createdTime,
  7: string shippingAddress
}

// Исключение для обработки ошибок
exception OrderException {
  1: string message,
  2: string errorCode
}

// Сервис для обработки заказов
service OrderService {
  // Создание нового заказа
  string createOrder(1: Order order) throws (1: OrderException ex),
  
  // Получение информации о заказе
  Order getOrder(1: string orderId) throws (1: OrderException ex),
  
  // Обновление статуса заказа
  bool updateOrderStatus(1: string orderId, 2: OrderStatus status) throws (1: OrderException ex),
  
  // Отмена заказа
  bool cancelOrder(1: string orderId) throws (1: OrderException ex),
  
  // Получение всех заказов клиента
  list<Order> getOrdersByCustomer(1: string customerId) throws (1: OrderException ex)
}
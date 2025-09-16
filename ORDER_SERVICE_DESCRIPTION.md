# Thrift Order Service

Это пример реализации Thrift сервиса для обработки заказов.

## Файлы

- `order_service.thrift` - Определение Thrift сервиса
- `server.py` - Реализация сервера
- `client.py` - Тестовый клиент

## Структура сервиса

### Структуры данных
- `Order`: Основная структура заказа
- `OrderRequest`: Запрос на создание заказа
- `OrderResponse`: Ответ на создание заказа
- `OrderException`: Исключение для обработки ошибок

### Методы сервиса
1. `createOrder`: Создание нового заказа
2. `getOrder`: Получение информации о заказе по ID
3. `updateOrderStatus`: Обновление статуса заказа
4. `listOrders`: Получение списка всех заказов

## Запуск

1. Запустите сервер:
   ```
   python3 server.py
   ```

2. В другом терминале запустите клиент:
   ```
   python3 client.py
   ```

## Требования

- Python 3.x
- thrift библиотека Python: `pip install thrift`
- thrift компилятор: `apt-get install thrift-compiler` (для Debian/Ubuntu)
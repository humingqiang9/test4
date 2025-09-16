// OrderStatusEnum.ts

/**
 * Enum representing the possible states of an order.
 */
enum OrderStatus {
    /** The order has been created but not yet processed. */
    Pending = 'pending',

    /** The order is being prepared or processed. */
    Processing = 'processing',

    /** The order has been shipped. */
    Shipped = 'shipped',

    /** The order has been delivered to the customer. */
    Delivered = 'delivered',

    /** The order has been cancelled. */
    Cancelled = 'cancelled',

    /** The order could not be completed due to an error. */
    Failed = 'failed'
}

export default OrderStatus;
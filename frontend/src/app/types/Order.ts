export interface OrderItem {
    name: string;
    quantity: number;
    price_per_unit: number;
    total: number;
}

export interface Order {
    created: string;
    subtotal: number;
    total: number;
    taxes: number;
    discounts: number;
    items: OrderItem[];
}
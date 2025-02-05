from backend.app.core.entities.order import Order
from backend.app.core.entities.stock import Stock
from backend.app.core.utils.apply_promotions import calculate_discount

def calculate_order_totals(order: Order, stock: Stock) -> Order:
    subtotal = 0
    beer_map = {beer.name: beer for beer in stock.beers}

    for order_round in order.rounds:
        for item in order_round.items:
            beer = beer_map.get(item.name)
            if beer:
                if beer.quantity >= item.quantity:
                    item.price_per_unit = beer.price
                    item.total = beer.price * item.quantity
                    subtotal += item.total

    taxes = int(subtotal * 0.15)

    promotion_rules = {
        "min_amount": 20,
        "discount_percentage": 10,
    }

    discount = calculate_discount(subtotal, promotion_rules)  # Uso de la función

    order.subtotal = subtotal
    order.taxes = taxes
    order.discount = discount
    order.items = [item for rnd in order.rounds for item in rnd.items]

    return order
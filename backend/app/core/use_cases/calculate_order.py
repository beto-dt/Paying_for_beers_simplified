from backend.app.core.entities.order import Order
from backend.app.core.entities.stock import Stock


def calculate_order_totals(order: Order, stock: Stock) -> Order:
    subtotal = 0
    beer_map = {beer.name: beer for beer in stock.beers.beers}

    for order_round in order.rounds:
        for item in order_round.items:
            beer = beer_map.get(item.name)
            if beer:
                if beer.quantity >= item.quantity:
                    item.price = beer.price = beer.price
                    item.total = beer.price * item.quantity
                    subtotal += item.total

    taxes = int(subtotal * 0.15)
    discount = 0

    order.subtotal = subtotal
    order.taxes = taxes
    order.discount = discount
    order.items = [item for rnd in order.rounds for item in rnd.items]

    return order
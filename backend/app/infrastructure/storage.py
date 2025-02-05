from datetime import datetime
from backend.app.core.entities.stock import Stock
from backend.app.core.entities.order import Order

stock_data = Stock(
    last_update=datetime(2024, 9, 10, 12, 0, 0),
    beers=[
        {"name": "Corona", "price": 115, "quantity": 5},
        {"name": "Quilmes", "price": 120, "quantity": 0},
        {"name": "Club Colombia", "price": 110, "quantity": 3},
    ],
)

order_data = Order(
    created=datetime(2024, 9, 10, 12, 0, 0),
    rounds=[
        {
            "created": datetime(2024, 9, 10, 12, 0, 30),
            "items": [
                {"name": "Corona", "quantity": 2},
                {"name": "Club Colombia", "quantity": 1},
            ],
        },
        {
            "created": datetime(2024, 9, 10, 12, 20, 0),
            "items": [
                {"name": "Club Colombia", "quantity": 1},
                {"name": "Quilmes", "quantity": 1},
            ],
        },
    ],
)
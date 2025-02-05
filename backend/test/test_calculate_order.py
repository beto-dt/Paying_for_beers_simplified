from backend.app.core.use_cases.calculate_order import  calculate_order_totals
from backend.app.infrastructure.storage import  stock_data, order_data

def test_order_totals():
    order = calculate_order_totals(order_data,stock_data)
    assert order.subtotal > 0
    assert order.tax > 0
    assert order.discount == 0

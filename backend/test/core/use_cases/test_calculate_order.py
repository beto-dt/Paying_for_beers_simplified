from backend.app.core.use_cases.calculate_order import  calculate_order_totals
from backend.app.infrastructure.storage import  stock_data, order_data

def test_order_totals_with_discount():
    order = calculate_order_totals(order_data, stock_data)
    expected_discount = 57.0
    assert order.subtotal > 0
    assert order.taxes > 0
    assert order.discount == expected_discount

from fastapi import APIRouter

from backend.app.core.use_cases.calculate_order import calculate_order_totals
from backend.app.infrastructure.storage import stock_data, order_data

router = APIRouter()


@router.get("/order/status", tags=["Order"])
def order_status():
    order = calculate_order_totals(order_data, stock_data)

    return {
        "order": {
            "created": order.created,
            "subtotal": order.subtotal,
            "total": order.subtotal + order.taxes - order.discount,
            "taxes": order.taxes,
            "discounts": order.discount,
            "items": [item.model_dump() for item in order.items],
        }
    }

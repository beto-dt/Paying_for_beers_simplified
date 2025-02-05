def calculate_discount(subtotal: float, promotion_rules: dict) -> float:
    discount = 0.0

    if promotion_rules:
        min_amount = promotion_rules.get("min_amount", 0)
        discount_percentage = promotion_rules.get("discount_percentage", 0)

        if subtotal >= min_amount:
            discount = subtotal * (discount_percentage / 100)

    return round(discount, 2)
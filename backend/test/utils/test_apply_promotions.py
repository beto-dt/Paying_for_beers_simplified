import pytest
from backend.app.core.utils.apply_promotions import calculate_discount

def test_calculate_discount_no_promotion_rules():
    subtotal = 150
    promotion_rules = None
    discount = calculate_discount(subtotal, promotion_rules)
    assert discount == 0.0

def test_calculate_discount_below_min_amount():
    subtotal = 80
    promotion_rules = {"min_amount": 100, "discount_percentage": 10}
    discount = calculate_discount(subtotal, promotion_rules)
    assert discount == 0.0

def test_calculate_discount_exact_min_amount():

    subtotal = 100
    promotion_rules = {"min_amount": 100, "discount_percentage": 10}
    discount = calculate_discount(subtotal, promotion_rules)
    assert discount == 10.0

def test_calculate_discount_above_min_amount():
    subtotal = 200
    promotion_rules = {"min_amount": 100, "discount_percentage": 15}
    discount = calculate_discount(subtotal, promotion_rules)
    assert discount == 30.0

def test_calculate_discount_zero_percentage():
    subtotal = 200
    promotion_rules = {"min_amount": 100, "discount_percentage": 0}
    discount = calculate_discount(subtotal, promotion_rules)
    assert discount == 0.0

def test_calculate_discount_no_min_amount_key():
    subtotal = 200
    promotion_rules = {"discount_percentage": 10}  # Sin `min_amount`
    discount = calculate_discount(subtotal, promotion_rules)
    assert discount == 20.0

def test_calculate_discount_no_discount_percentage_key():
    subtotal = 200
    promotion_rules = {"min_amount": 100}  # Sin `discount_percentage`
    discount = calculate_discount(subtotal, promotion_rules)
    assert discount == 0.0
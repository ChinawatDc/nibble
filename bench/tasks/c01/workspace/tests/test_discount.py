from shop.pricing.discount import apply_discount

def test_exact():
    assert apply_discount(1000) == 950.0

from collections import Counter

PRICES = {
    "A": {"price": 50, "special": {"count": 3, "price": 130}},
    "B": {"price": 30, "special": {"count": 2, "price": 45}},
    "C": {"price": 20, "special": None},
    "D": {"price": 15, "special": None},
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = Counter(skus)
    total = 0
    for sku, count in counts.items():
        # Check for specials
        special = PRICES[sku]["special"]
        if special:
            special_count, count = divmod(count, special["count"])
            total += special_count * special["price"]
        # Add remaining count
        total += count * PRICES[sku]["price"]

    return total



assert checkout("A") == 50
assert checkout("B") == 30
assert checkout("C") == 20
assert checkout("D") == 15

assert checkout("A") == 50


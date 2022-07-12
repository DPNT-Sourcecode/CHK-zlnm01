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
        sku_prices = PRICES.get(sku)
        if not sku_prices:
            return -1

        # Check for specials
        special = sku_prices["special"]
        if special:
            special_count, count = divmod(count, special["count"])
            total += special_count * special["price"]
        # Add remaining count
        total += count * sku_prices["price"]

    return total

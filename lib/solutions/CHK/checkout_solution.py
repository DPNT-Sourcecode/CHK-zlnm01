from collections import Counter
from typing import Tuple

PRICES = {
    "A": {"price": 50, "special": [{"count": 5, "price": 200}, {"count": 3, "price": 130}]},
    "B": {"price": 30, "special": [{"count": 2, "price": 45}]},
    "C": {"price": 20, "special": []}, # easier but less memory efficient
    "D": {"price": 15, "special": []}, # easier but less memory efficient
    "E": {"price": 40, "special": [{"count": 2, "bonus": "B"}]},
}
PRICE_ORDER = ("E", "D", "C", "B", "A")

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = Counter(skus)
    # Check for any invalid items
    if not set(PRICES.keys()).issuperset(counts.keys()):
        return -1

    total = 0
    for sku in PRICE_ORDER:
        if sku not in counts:
            continue

        # Apply best price to total
        best_price = _calculate_prices(PRICES[sku], counts[sku])
        total += best_price[0]
        # Apply bonus
        bonus = best_price[1]
        if bonus:
            # Assumes all bonus letters are the same
            counts.subtract(bonus)
            if counts[bonus[0]] < 0:
                counts[bonus[0]] = 0

    return total

def _calculate_prices(sku_prices: dict, count) -> Tuple[int, str]:
    # returns price and bonus
    specials = sku_prices["special"]
    # Hacky check for bonus specials
    if specials and "bonus" in specials[0]:
        return _calculate_bonus(
            count,
            specials[0]["count"],
            specials[0]["bonus"],
            sku_prices["price"]
        )

    # Run normal specials
    total = 0
    for special in specials:
        special_count, count = divmod(count, special["count"])
        total += special_count * special["price"]

    # Add normal price
    total += count * sku_prices["price"]
    return (total, "")

def _calculate_bonus(count, offer_count, bonus, default_price) -> Tuple[int, str]:
    special_count = count // offer_count
    return (count * default_price, bonus * special_count)

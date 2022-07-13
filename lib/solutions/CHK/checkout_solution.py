from collections import Counter
from typing import Tuple

PRICES = {
    "A": [{"count": 5, "price": 200}, {"count": 3, "price": 130}, {"price": 50}],
    "B": [{"count": 2, "price": 45}, {"price": 30}],
    "C": [{"price": 20}],
    "D": [{"price": 15}],
    "E": [{"count": 2, "bonus": "B"}, {"price": 40}],
    "F": [{"count": 3, "price": 20}, {"price": 10}],
}
PRICE_ORDER = ("F", "E", "D", "C", "B", "A")

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
    total = 0
    bonus = ""
    for price in sku_prices:
        p_count = price.get("count", 1)
        new_bonus = _calculate_bonus(count, p_count, price.get("bonus"))
        # Don't price bonus offers
        if new_bonus:
            bonus += new_bonus
            continue

        price_count, count = divmod(count, p_count)
        total += price_count * price["price"]

    return (total, bonus)


def _calculate_bonus(count, offer_count, bonus) -> str:
    if not bonus:
        return ""
    special_count = count // offer_count
    return bonus * special_count

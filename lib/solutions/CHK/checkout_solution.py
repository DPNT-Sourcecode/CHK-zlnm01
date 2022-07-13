from collections import Counter
from typing import Tuple

PRICES = {
    "A": [{"count": 5, "price": 200}, {"count": 3, "price": 130}, {"price": 50}],
    "B": [{"count": 2, "price": 45}, {"price": 30}],
    "C": [{"price": 20}],
    "D": [{"price": 15}],
    "E": [{"count": 2, "bonus": "B"}, {"price": 40}],
    "F": [{"count": 3, "price": 20}, {"price": 10}],
    "G": [{"price": 20}],
    "H": [{"count": 10, "price": 80}, {"count": 5, "price": 45}, {"price": 10}],
    "I": [{"price": 35}],
    "J": [{"price": 60}],
    "K": [{"count": 2, "price": 120}, {"price": 70}],
    "L": [{"price": 90}],
    "M": [{"price": 15}],
    "N": [{"count": 3, "bonus": "M"}, {"price": 40}],
    "O": [{"price": 10}],
    "P": [{"count": 5, "price": 200}, {"price": 50}],
    "Q": [{"count": 3, "price": 80}, {"price": 30}],
    "R": [{"count": 3, "bonus": "Q"}, {"price": 50}],
    "S": [{"price": 20}],
    "T": [{"price": 20}],
    "U": [{"count": 4, "price": 120}, {"price": 40}],
    "V": [{"count": 3, "price": 130}, {"count": 2, "price": 90}, {"price": 50}],
    "W": [{"price": 20}],
    "X": [{"price": 17}],
    "Y": [{"price": 20}],
    "Z": [{"price": 21}],
}
# Luckily any bonus is always given to an SKU earlier in the alphabet
PRICE_ORDER = sorted(PRICES.keys(), reverse=True)

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = Counter(skus)
    # Check for any invalid items
    if not set(PRICES.keys()).issuperset(counts.keys()):
        return -1

    # Apply any multibuy offers first as cheaper
    total = apply_multibuy(counts)

    for sku in PRICE_ORDER:
        if sku not in counts:
            continue

        # Apply best price to total
        total += _calculate_prices(PRICES[sku], counts[sku], counts)

    return total


def _calculate_prices(sku_prices: dict, count: int, counts: Counter) -> int:
    # returns price and bonus
    total = 0
    for price in sku_prices:
        p_count = price.get("count", 1)
        if _apply_bonus(count, p_count, price.get("bonus"), counts):
            continue

        price_count, count = divmod(count, p_count)
        total += price_count * price["price"]

    return total


def _apply_bonus(count, offer_count, bonus, counts: Counter) -> bool:
    if not bonus:
        return False

    special_count = count // offer_count
    # Subtract bonus from counts
    counts.subtract(bonus * special_count)
    # Ensure no negative counts
    if counts[bonus] < 0:
        counts[bonus] = 0
    return True


MULTIBUY_SKUS = ("Z", "Y", "S", "T", "X")
MULTIBUY_COUNT = 3
MULTIBUY_PRICE = 45


def apply_multibuy(counts: Counter) -> int:
    """Checks for existence of multibuy values, finds most expensive combo and applies"""
    multis = []
    for sku in MULTIBUY_SKUS:
        multis.extend((sku, PRICES[sku][0]["price"]) for _ in range(counts[sku]))
    multis.sort(key=lambda m: m[1], reverse=True)

    # Calculate eligible multibuy offers
    multi_count = len(multis) // MULTIBUY_COUNT
    # Remove multibuy skus from counts
    counts.subtract(m[0] for m in multis[: multi_count * MULTIBUY_COUNT])
    return multi_count * MULTIBUY_PRICE






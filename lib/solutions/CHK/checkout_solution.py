from collections import Counter
from .constants import (
    PRICES,
    PRICE_ORDER,
    MULTIBUY_COUNT,
    MULTIBUY_PRICE,
    MULTIBUY_SKUS,
)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = Counter(skus)
    # Check for any invalid items
    if not set(PRICES.keys()).issuperset(counts.keys()):
        return -1

    # Apply any multibuy offers first as cheaper
    total = _apply_multibuy(counts)

    for sku in PRICE_ORDER:
        if sku not in counts:
            continue

        # Apply best price to total
        total += _calculate_prices(PRICES[sku], counts[sku], counts)

    return total


def _calculate_prices(sku_prices: dict, count: int, counts: Counter) -> int:
    """Finds best offer combinations
    Assumes that offers are in order of most price efficient
    and no combo will be better than giving most of each offer level.
    """
    total = 0
    for price in sku_prices:
        p_count = price.get("count", 1)
        if _apply_bonus(count, p_count, price.get("bonus"), counts):
            continue

        price_count, count = divmod(count, p_count)
        total += price_count * price["price"]

    return total


def _apply_bonus(count, offer_count, bonus, counts: Counter) -> bool:
    """Checks if price is a bonus and removes bonus SKUs from price

    Requires SKUs to be iterated in correct order
    Does not apply a price from bonus (unchecked)
    """
    if not bonus:
        return False

    special_count = count // offer_count
    # Subtract bonus from counts
    counts.subtract(bonus * special_count)
    # Ensure no negative counts
    if counts[bonus] < 0:
        counts[bonus] = 0
    return True


def _apply_multibuy(counts: Counter) -> int:
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








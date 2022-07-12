from collections import Counter
from typing import List, Tuple

PRICES = {
    "A": {"price": 50, "special": [{"count": 3, "price": 130}, {"count": 5, "price": 200}]},
    "B": {"price": 30, "special": [{"count": 2, "price": 45}]},
    "C": {"price": 20, "special": None},
    "D": {"price": 15, "special": None},
    "E": {"price": 40, "special": [{"count": 2, "bonus": "B"}]},
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

        # Add remaining count
        prices = _calculate_prices(sku_prices, count)
        prices.sort(key=lambda t: t[0])
        # Apply best price to total
        total += prices[-1][0]

    return total

def _calculate_prices(sku_prices: dict, count) -> List[Tuple[int, str]]:
    # returns list of prices and bonuses
    prices = []
    default_price = sku_prices["price"]
    # Check for specials
    for special in sku_prices["special"]:
        if "price" in special:
            prices.append(_calculate_special_price(count, special["count"], special["price"], default_price))
        elif "bonus" in special:
            prices.append(_calculate_bonus(count, special["count"], special["bonus"], default_price))
    # Add normal price
    prices.append((count * sku_prices["price"], None))
    return prices


def _calculate_special_price(count, offer_count, special_price, default_price) -> Tuple[int, None]:
    special_count, rem = divmod(count, offer_count)
    return (special_count * special_price + rem * default_price, None)

def _calculate_bonus(count, special_count, bonus, default_price) -> Tuple[int, str]:
    special_count = count % special_count
    return (count * default_price, bonus * special_count)


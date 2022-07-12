from collections import Counter
from typing import List, Tuple

PRICES = {
    "A": {"price": 50, "special": [{"count": 3, "price": 130}, {"count": 5, "price": 200}]},
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

        sku_prices = PRICES[sku]
        # if not sku_prices:
        #     return -1

        prices = _calculate_prices(sku_prices, counts[sku])
        prices.sort(key=lambda t: t[0])

        # Apply best price to total
        best_price = prices[0]
        total += best_price[0]
        # Apply bonus
        bonus = best_price[1]
        if bonus:
            # Assumes all bonus letters are the same
            counts[bonus[0]] -= len(bonus)


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





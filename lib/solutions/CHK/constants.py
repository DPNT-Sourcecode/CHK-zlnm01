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


MULTIBUY_SKUS = ("Z", "Y", "S", "T", "X")
MULTIBUY_COUNT = 3
MULTIBUY_PRICE = 45

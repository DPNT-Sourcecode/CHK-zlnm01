from checkout_solution import checkout


# CHK_R1 test
assert checkout("A") == 50
assert checkout("B") == 30
assert checkout("C") == 20
assert checkout("D") == 15

print(checkout("AAAA"))
assert checkout("AAAA") == 180
assert checkout("BBBBB") == 120


assert checkout("DABCABCABC") == 130 + 45 + 30 + 20 * 3 + 15

assert checkout("DEF") == -1
assert checkout("a") == -1

# CHK_R2 test

# EEB asserts
print(checkout("EEB"))
assert checkout("EEB") == 80
assert checkout("BEE") == 80
assert checkout("EBE") == 80
assert checkout("EBEEBBEB") == 125

# Multi A asserts
assert checkout("AAAAA") == 200
print(checkout("AAAAAAAA"))
assert checkout("AAAAAAAA") == 330
assert checkout("AAAAAAAAA") == 380
assert checkout("AAAAAAAAAA") == 400
assert checkout("AAAAAAAAAAA") == 450 # cheaper than 5 + 2 * 3, assume rule generally holds so don't need to check all combos of discounts





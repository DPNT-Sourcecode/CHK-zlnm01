from checkout_solution import checkout


# CHK_R1 test
assert checkout("A") == 50
assert checkout("B") == 30
assert checkout("C") == 20
assert checkout("D") == 15

assert checkout("AAAA") == 180
assert checkout("BBBBB") == 120


assert checkout("DABCABCABC") == 130 + 45 + 30 + 20 * 3 + 15

assert checkout("DEF") == -1
assert checkout("a") == -1

# CHK_R2 test


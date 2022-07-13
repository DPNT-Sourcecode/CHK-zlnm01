import unittest

from parameterized import parameterized

from checkout_solution import checkout


class Test(unittest.TestCase):
    @parameterized.expand(
        [
            # CHK_R1 test
            ("A", 50),
            ("B", 30),
            ("C", 20),
            ("D", 15),
            ("AAAA", 180),
            ("BBBBB", 120),
            ("DABCABCABC", 130 + 45 + 30 + 20 * 3 + 15),
            # Invalid
            ("DEY", -1),
            ("a", -1),
            # CHK_R2 test
            # EEB asserts
            ("EE", 80),
            ("EEB", 80),
            ("BEE", 80),
            ("EBE", 80),
            ("EBEEBBEB", 160 + 45),
            # Multi A asserts
            ("AAAAA", 200),
            ("AAAAAAAA", 330),
            ("AAAAAAAAA", 380),
            ("AAAAAAAAAA", 400),
            # cheaper than 5 + 2 * 3, assume rule generally holds so don't need to check all combos of discounts
            ("AAAAAAAAAAA", 450),
            # CHK_R3 test
            ("F", 10),
            ("FF", 20),
            ("FFF", 20),
            ("FFFF", 30),
            ("FFFFF", 40),
            ("FFFFFF", 40),
        ]
    )
    def test_checkout_price(self, input, expected):
        self.assertEqual(checkout(input), expected)



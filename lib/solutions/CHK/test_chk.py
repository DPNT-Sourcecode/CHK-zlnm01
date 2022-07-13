import unittest

from parameterized import parameterized

from checkout_solution import checkout


class Test(unittest.TestCase):
    @parameterized.expand(
        [
            # CHK_R1 test
            ("", 0),
            ("A", 50),
            ("B", 30),
            ("C", 20),
            ("D", 15),
            ("AAAA", 180),
            ("BBBBB", 120),
            ("DABCABCABC", 130 + 45 + 30 + 20 * 3 + 15),
            # Invalid
            ("a", -1),
            ("DEy", -1),
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
            # CHK_R4 test
            ("DEY", 75),
            ("G", 20),
            ("H", 10),
            ("H" * 16, 80 + 45 + 10),
            ("I", 35),
            ("J", 60),
            ("K", 70),
            ("K" * 3, 120 + 70),
            ("L", 90),
            ("M", 15),
            ("N", 40),
            ("MNNNNMM", 4 * 40 + 2 * 15),
            ("O", 10),
            ("P", 50),
            ("P" * 6, 200 + 50),
            ("Q", 30),
            ("Q" * 4, 80 + 30),
            ("R", 50),
            ("RRRRQQ", 50 * 4 + 1 * 30),
            ("S", 20),
            ("T", 20),
            ("U", 40),
            ("U" * 5, 120 + 40),
            ("V", 50),
            ("V" * 7, 130 * 2 + 50),
            ("V" * 5, 130 + 90),
            ("W", 20),
            ("X", 17),
            ("Y", 20),
            ("Z", 21),
        ]
    )
    def test_checkout_price(self, input, expected):
        self.assertEqual(checkout(input), expected)


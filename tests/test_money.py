import unittest

from src.pcr_money.money import Money

class TestMoney(unittest.TestCase):
    def test_handle_value_round(self):
        self.assertEqual(Money.handle_value(10.774,2,"round"),10.77)
        self.assertEqual(Money.handle_value(10.777,2,"round"),10.78)
        self.assertEqual(Money.handle_value(10.77,2,"round"),10.77)

    def test_handle_value_truncation(self):
        self.assertEqual(Money.handle_value(10.774,2,"truncation"),10.77)
        self.assertEqual(Money.handle_value(10.777,2,"truncation"),10.77)
        self.assertEqual(Money.handle_value(10.771,2,"truncation"),10.77)

if __name__ == "__name__":
    unittest.main()
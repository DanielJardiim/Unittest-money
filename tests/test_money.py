import unittest

from src.money.money import Money

class TestMoney(unittest.TestCase):
    def test_value_round_baixo(self):
        valor1 = Money.value(10.774,2,"round")
        self.assertEqual(valor1,10.77)
        
    def test_value_round_alto(self):
        valor2 = Money.value(10.778,2,"round")
        self.assertEqual(valor2,10.78)

    def test_value_round_mantem(self):
        valor3 = Money.value(10.77,2,"round")
        self.assertEqual(valor3,10.77)

    def test_value_truncation_baixo(self):
        valor4 = Money.value(10.774,2,"truncation")
        self.assertEqual(valor4,10.77)

    def test_value_truncation_alto(self):
        valor5 = Money.value(10.778,2,"truncation")
        self.assertEqual(valor5,10.77)

    def test_value_truncation_mantem(self):
        valor6 = Money.value(10.77,2,"truncation")
        self.assertEqual(valor6,10.77)

    def test_value_error_method(self):
        valor7 = Money.value(10.568,2,"error")
        self.assertFalse(valor7)
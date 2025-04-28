import unittest

# Предполагается, что функция находится в файле, например, payment_calculator.py
from functions.calculate_payment_for_period import calculate_payment_for_period

class TestPaymentCalculator(unittest.TestCase):
    def test_calculate_payment_for_period(self):
        # Тестовый случай 1: базовые значения
        self.assertEqual(calculate_payment_for_period(100, 30, 10), 5000)
        
        # Тестовый случай 2: нулевые значения
        self.assertEqual(calculate_payment_for_period(0, 30, 10), 0)
        self.assertEqual(calculate_payment_for_period(100, 0, 0), 0)
        
        
        # Тестовый случай 4: большие значения
        self.assertEqual(calculate_payment_for_period(1000000, 1000, 500), 2000000000)

    def test_calculate_payment_for_period_with_zero_value(self):
        # Тестовый случай: нулевое значение
        self.assertEqual(calculate_payment_for_period(0, 30, 10), 0)

    def test_calculate_payment_for_period_with_zero_days(self):
        # Тестовый случай: нулевые дни
        self.assertEqual(calculate_payment_for_period(100, 0, 0), 0)

if __name__ == '__main__':
    unittest.main()
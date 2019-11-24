# [USAGE]: python -m unittest tests/calculator_test.py
import unittest
import calculator
from calculator import NotMatchArgvError
from calculator import NotMatchNumError
from calculator import NotIncludeError


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.argv = ['file_name', '5', '4', '+']

    def test_check_validate(self):
        calculator.check_validate(self.argv)

    def test_invalid_not_match_value(self):
        self.argv = []
        with self.assertRaises(NotMatchArgvError):
            calculator.check_validate(self.argv)

    def test_invalid_first_value(self):
        self.argv[1] = 'a'
        with self.assertRaises(NotMatchNumError):
            calculator.check_validate(self.argv)

    def test_invalid_second_value(self):
        self.argv[2] = 'a'
        with self.assertRaises(NotMatchNumError):
            calculator.check_validate(self.argv)

    def test_not_include_error_value(self):
        self.argv[3] = 'a'
        with self.assertRaises(NotIncludeError):
            calculator.check_validate(self.argv)


class TestIsDigit(unittest.TestCase):
    def test_is_digit_true(self):
        self.assertEqual(calculator.is_digit(str(1)), True)

    def test_is_digit_true_minus(self):
        self.assertEqual(calculator.is_digit(str(-1)), True)

    def test_is_digit_false(self):
        self.assertEqual(calculator.is_digit('a'), False)


class TestCaluculate(unittest.TestCase):
    def setUp(self):
        self.first = 8
        self.second = 4
        self.operator = '+'

    def test_caluculate_plus(self):
        self.assertEqual(
            calculator.calculate(self.first, self.second, self.operator), 12)

    def test_caluculate_minus(self):
        self.operator = '-'
        self.assertEqual(
            calculator.calculate(self.first, self.second, self.operator), 4)

    def test_caluculate_multiplication(self):
        self.operator = '*'
        self.assertEqual(
            calculator.calculate(self.first, self.second, self.operator), 32)

    def test_caluculate_division(self):
        self.operator = '/'
        self.assertEqual(
            calculator.calculate(self.first, self.second, self.operator), 2)

    def test_caluculate_zero_division_error(self):
        self.second = 0
        self.operator = '/'
        with self.assertRaises(ZeroDivisionError):
            calculator.calculate(self.first, self.second, self.operator)

    def test_caluculate_not_include_error(self):
        self.operator = 'a'
        with self.assertRaises(NotIncludeError):
            calculator.calculate(self.first, self.second, self.operator)

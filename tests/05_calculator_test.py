import unittest
import calculator
from calculator import NotMatchArgvError
from calculator import NotMatchNumError
from calculator import NotIncludeError

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.argv = ['file_name', '5', '4', '+']

    def test_check_validate(self):
        // エラーが起きないことを確認する
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



from unittest import TestCase, main
from lessons.calculator import calculator

class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator("2+3"), 5)

    def test_minus(self):
        self.assertEqual(calculator("25-10"), 15)

    def test_multi(self):
        self.assertEqual(calculator("10*10"), 100)

    def test_divide(self):
        self.assertEqual(calculator("40/5"), 8.0)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("abracadabra")
        self.assertEqual("The expression must contain at least 1 character (+-*/)!", e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+2+2")
        self.assertEqual("The expression must contain 2 integer nums and 1 character!", e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator("2+3*10")
        self.assertEqual("The expression must contain 2 integer nums and 1 character!", e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator("2.34+34.98")
        self.assertEqual("The expression must contain 2 integer nums and 1 character!", e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator("a+b")
        self.assertEqual("The expression must contain 2 integer nums and 1 character!", e.exception.args[0])






if __name__ == '__main__':
    main()
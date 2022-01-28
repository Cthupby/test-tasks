import unittest


def is_even(number):
    ''' Returns True if **number** is even or False if it is odd. '''
    return number % 2


class TestValidEven(unittest.TestCase):
    ''' Returns True if **number** is even '''
    def test_even_numbers(self):
        for number in 4, 22:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), True)
    ''' Returns False if it is odd. '''
    def test_other_numbers(self):
        for number in 3, 59:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), False)


if __name__ == "__main__":
    unittest.main()

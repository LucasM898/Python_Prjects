import random
import unittest
def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'
class Test_the_function(unittest.TestCase):
    def test_one(self):
        for x in range(100):
            number1 = random.randint(-1000, 1000)
            result = ''
            if number1 % 2 == 0:
                result = 'Even'
            else:
                result = 'Odd'
            self.assertEqual(even_or_odd(number1), result)
if __name__ == '__main__':
    unittest.main()

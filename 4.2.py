import unittest

class FibonacciCalculator:
    def calculate(self, n):
        if n <= 0:
            raise ValueError("n должно быть положительным целым числом")
        
        fibonacci_numbers = [0, 1]
        
        while len(fibonacci_numbers) < n:
            next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
            fibonacci_numbers.append(next_number)
        
        return fibonacci_numbers[:n]

class TestFibonacciCalculator(unittest.TestCase):
    def test_calculate_with_positive_n(self):
        calculator = FibonacciCalculator()
        result = calculator.calculate(5)
        self.assertEqual(result, [0, 1, 1, 2, 3])

    def test_calculate_with_zero_n(self):
        calculator = FibonacciCalculator()
        with self.assertRaises(ValueError):
            calculator.calculate(0)

    def test_calculate_with_negative_n(self):
        calculator = FibonacciCalculator()
        with self.assertRaises(ValueError):
            calculator.calculate(-3)

if __name__ == '__main__':
    unittest.main()
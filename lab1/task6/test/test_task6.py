import unittest
from lab1.task6.src.task6 import largest_salary_number, compare


class TestLargestSalaryNumber(unittest.TestCase):

    def test_single_digit_numbers(self):
        # Given: Подготовка данных
        numbers = [3, 30, 34, 5, 9]

        # When: Выполнение функции
        result = largest_salary_number(numbers)

        # Then: Проверка результата
        self.assertEqual(result, '9534330')

    def test_all_zeroes(self):
        # Given: Подготовка данных
        numbers = [0, 0, 0]

        # When: Выполнение функции
        result = largest_salary_number(numbers)

        # Then: Проверка результата
        self.assertEqual(result, '0')

    def test_mixed_numbers(self):
        # Given: Подготовка данных
        numbers = [10, 2]

        # When: Выполнение функции
        result = largest_salary_number(numbers)

        # Then: Проверка результата
        self.assertEqual(result, '210')

    def test_large_numbers(self):
        # Given: Подготовка данных
        numbers = [60, 6, 597]

        # When: Выполнение функции
        result = largest_salary_number(numbers)

        # Then: Проверка результата
        self.assertEqual(result, '660597')

    def test_repeated_digits(self):
        # Given: Подготовка данных
        numbers = [823, 82]

        # When: Выполнение функции
        result = largest_salary_number(numbers)

        # Then: Проверка результата
        self.assertEqual(result, '82823')

    def test_variety_of_inputs(self):
        # Given: Подготовка данных
        numbers = [1, 2, 3, 9, 30, 31]

        # When: Выполнение функции
        result = largest_salary_number(numbers)

        # Then: Проверка результата
        self.assertEqual(result, '93313021')


if __name__ == '__main__':
    unittest.main()
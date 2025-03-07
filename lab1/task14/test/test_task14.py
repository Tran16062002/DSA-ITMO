import unittest
from lab1.task14.src.task14 import max_expression_value


class TestMaxExpressionValue(unittest.TestCase):

    def test_simple_expressions(self):
        # Given: Подготовка данных
        expr = "1+2*3"

        # When: Выполнение функции
        result = max_expression_value(expr)

        # Then: Проверка результата
        self.assertEqual(result, 9)

    def test_mixed_operations(self):
        # Given: Подготовка данных
        expr = "1*2+3*4"

        # When: Выполнение функции
        result = max_expression_value(expr)

        # Then: Проверка результата
        self.assertEqual(result, 20)

    def test_edge_cases(self):
        # Given: Подготовка данных
        expr = "3*1*2"

        # When: Выполнение функции
        result = max_expression_value(expr)

        # Then: Проверка результата
        self.assertEqual(result, 6)

    def test_zero_and_negative_numbers(self):
        # Given: Подготовка данных
        expr = "1-1-1"

        # When: Выполнение функции
        result = max_expression_value(expr)

        # Then: Проверка результата
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
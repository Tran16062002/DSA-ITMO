import unittest
from lab4.task6.src.task6 import z_function

# Тесты
class TestZFunction(unittest.TestCase):
    def test_basic_case(self):
        # Given: Подготовка данных
        s = "abacaba"
        expected = [0, 0, 1, 0, 3, 0, 1]

        # When: Выполнение функции
        result = z_function(s)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_full_repeats(self):
        # Given: Подготовка данных
        s = "aaaaaa"
        expected = [0, 5, 4, 3, 2, 1]

        # When: Выполнение функции
        result = z_function(s)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_no_matches(self):
        # Given: Подготовка данных
        s = "abcdef"
        expected = [0, 0, 0, 0, 0, 0]

        # When: Выполнение функции
        result = z_function(s)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_overlap(self):
        # Given: Подготовка данных
        s = "aabcaabxaaaz"
        expected = [0, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0]

        # When: Выполнение функции
        result = z_function(s)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_short_string(self):
        # Given: Подготовка данных
        s = "ab"
        expected = [0, 0]

        # When: Выполнение функции
        result = z_function(s)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_prefix_suffix(self):
        # Given: Подготовка данных
        s = "abcababcab"
        expected = [0, 0, 0, 2, 0, 3, 0, 0, 3, 0]

        # When: Выполнение функции
        result = z_function(s)

        # Then: Проверка результата
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

import unittest
from lab4.task1.src.task1 import naive_substring_search

class TestNaiveSubstringSearch(unittest.TestCase):
    def test_example(self):
        # Given: Подготовка данных
        p = "aba"
        t = "abacaba"
        positions = [1, 5]

        # When: Выполнение функции
        result = naive_substring_search(p, t)

        # Then: Проверка результата
        self.assertEqual(result, positions)

    def test_no_occurrence(self):
        # Given: Подготовка данных
        p = "abc"
        t = "aaaaa"
        positions = []
        # When: Выполнение функции
        result = naive_substring_search(p, t)

        # Then: Проверка результата
        self.assertEqual(result, positions)

    def test_full_match(self):
        # Given: Подготовка данных
        p = "abc"
        t = "abc"
        positions = [1]

        # When: Выполнение функции
        result = naive_substring_search(p, t)

        # Then: Проверка результата
        self.assertEqual(result, positions)

    def test_multiple_overlap(self):
        # Given: Подготовка данных
        p = "aa"
        t = "aaaaa"
        positions = [1, 2, 3, 4]

        # When: Выполнение функции
        result = naive_substring_search(p, t)

        # Then: Проверка результата
        self.assertEqual(result, positions)

    def test_pattern_longer_than_text(self):
        # Given: Подготовка данных
        p = "abcd"
        t = "abc"
        positions = []

        # When: Выполнение функции
        result = naive_substring_search(p, t)

        # Then: Проверка результата
        self.assertEqual(result, positions)

    def test_one_char(self):
        # Given: Подготовка данных
        p = "a"
        t = "banana"
        positions = [2, 4, 6]

        # When: Выполнение функции
        result = naive_substring_search(p, t)

        # Then: Проверка результата
        self.assertEqual(result, positions)

if __name__ == '__main__':
    unittest.main()

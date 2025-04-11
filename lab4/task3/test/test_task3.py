import unittest
from lab4.task3.src.task3 import rabin_karp

class TestRabinKarp(unittest.TestCase):
    def test_example1(self):
        # Given: Подготовка данных
        pattern = "aba"
        text = "abacaba"
        expected = [1, 5]

        # When: Выполнение функции
        result = rabin_karp(pattern, text)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_example2(self):
        # Given: Подготовка данных
        pattern = "Test"
        text = "testTesttesT"
        expected = [5]

        # When: Выполнение функции
        result = rabin_karp(pattern, text)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_example3(self):
        # Given: Подготовка данных
        pattern = "aaaaa"
        text = "baaaaaaa"
        expected = [2, 3, 4]

        # When: Выполнение функции
        result = rabin_karp(pattern, text)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_no_match(self):
        # Given: Подготовка данных
        pattern = "xyz"
        text = "abcdefgh"
        expected = []

        # When: Выполнение функции
        result = rabin_karp(pattern, text)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_full_match(self):
        # Given: Подготовка данных
        pattern = "abc"
        text = "abc"
        expected = [1]

        # When: Выполнение функции
        result = rabin_karp(pattern, text)

        # Then: Проверка результата
        self.assertEqual(result, expected)

    def test_overlapping(self):
        # Given: Подготовка данных
        pattern = "aa"
        text = "aaaa"
        expected = [1, 2, 3]

        # When: Выполнение функции
        result = rabin_karp(pattern, text)

        # Then: Проверка результата
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

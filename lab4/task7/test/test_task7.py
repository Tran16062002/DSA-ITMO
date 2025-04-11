import unittest
from lab4.task7.src.task7 import longest_common_substring

class TestLongestCommonSubstring(unittest.TestCase):
    def test_example_1(self):
        # Given: Подготовка данных
        s = "cool"
        t = "toolbox"

        # When: Выполнение функции
        i, j, l = longest_common_substring(s, t)

        # Then: Проверка результата
        self.assertEqual(l, 3)
        self.assertEqual(s[i:i+l], t[j:j+l])

    def test_example_2(self):
        # Given: Подготовка данных
        s = "aaa"
        t = "bb"

        # When: Выполнение функции
        i, j, l = longest_common_substring(s, t)

        # Then: Проверка результата
        self.assertEqual(l, 0)

    def test_example_3(self):
        # Given: Подготовка данных
        s = "aabaa"
        t = "babbaab"

        # When: Выполнение функции
        i, j, l = longest_common_substring(s, t)

        # Then: Проверка результата
        self.assertEqual(l, 3)
        self.assertEqual(s[i:i+l], t[j:j+l])

    def test_empty(self):
        # Given: Подготовка данных
        s = ""
        t = "abc"

        # When: Выполнение функции
        i, j, l = longest_common_substring(s, t)

        # Then: Проверка результата
        self.assertEqual(l, 0)

    def test_full_match(self):
        # Given: Подготовка данных
        s = "abcde"
        t = "abcde"

        # When: Выполнение функции
        i, j, l = longest_common_substring(s, t)

        # Then: Проверка результата
        self.assertEqual(l, 5)
        self.assertEqual(s[i:i+l], t[j:j+l])

    def test_overlap_multiple(self):
        # Given: Подготовка данных
        s = "ababc"
        t = "babc"

        # When: Выполнение функции
        i, j, l = longest_common_substring(s, t)

        # Then: Проверка результата
        self.assertEqual(s[i:i+l], t[j:j+l])
        self.assertEqual(l, 4)

if __name__ == '__main__':
    unittest.main()

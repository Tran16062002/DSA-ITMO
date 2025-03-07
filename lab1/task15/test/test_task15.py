import unittest
from lab1.task15.src.task15 import longest_valid_bracket_sequence


class TestLongestValidBracketSequence(unittest.TestCase):

    def test_valid_sequences(self):
        # Given: Подготовка данных
        s = "{[()]}[{}]"

        # When: Выполнение функции
        result = longest_valid_bracket_sequence(s)

        # Then: Проверка результата
        self.assertEqual(result, "{[()]}[{}]")

    def test_invalid_sequences(self):
        # Given: Подготовка данных
        s = "{[()]"

        # When: Выполнение функции
        result = longest_valid_bracket_sequence(s)

        # Then: Проверка результата
        self.assertEqual(result, "[()]")

    def test_mixed_valid_invalid_sequences(self):
        # Given: Подготовка данных
        s = "{[()]}()([]){}"

        # When: Выполнение функции
        result = longest_valid_bracket_sequence(s)

        # Then: Проверка результата
        self.assertEqual(result, "{[()]}()([]){}")

    def test_empty_string(self):
        # Given: Подготовка данных
        s = ""

        # When: Выполнение функции
        result = longest_valid_bracket_sequence(s)

        # Then: Проверка результата
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
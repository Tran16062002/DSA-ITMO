import unittest
from lab2.task16.src.task16 import process_commands

class TestProcessCommands(unittest.TestCase):
    def test_add_and_find_kth_max(self):
        # Given: Подготовка данных
        commands = [(+1, 10), (+1, 20), (+1, 30), (0, 1), (0, 2), (0, 3)]

        # When: Выполнение функции
        result = process_commands(len(commands), commands)

        # Then: Проверка результата
        self.assertEqual(result, [30, 20, 10])

    def test_delete_element(self):
        # Given: Подготовка данных
        commands = [(+1, 10), (+1, 20), (+1, 30), (-1, 20), (0, 1), (0, 2)]

        # When: Выполнение функции
        result = process_commands(len(commands), commands)

        # Then: Проверка результата
        self.assertEqual(result, [30, 10])

    def test_k_out_of_bounds(self):
        # Given: Подготовка данных
        commands = [(+1, 5), (+1, 15), (0, 3)]

        # When: Выполнение функции
        result = process_commands(len(commands), commands)

        # Then: Проверка результата
        self.assertEqual(result, [None])

    def test_empty_list_find_k(self):
        # Given: Подготовка данных
        commands = [(0, 1)]

        # When: Выполнение функции
        result = process_commands(len(commands), commands)

        # Then: Проверка результата
        self.assertEqual(result, [None])

    def test_duplicate_elements(self):
        # Given: Подготовка данных
        commands = [(+1, 10), (+1, 20), (+1, 10), (0, 1), (0, 2), (0, 3)]

        # When: Выполнение функции
        result = process_commands(len(commands), commands)

        # Then: Проверка результата
        self.assertEqual(result, [20, 10, 10])

if __name__ == "__main__":
    unittest.main()

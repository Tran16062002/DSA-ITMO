import unittest
from lab1.task13.src.task13 import can_partition


class TestCanPartition(unittest.TestCase):

    def test_partition_possible(self):
        # Given: Подготовка данных
        v = [1, 1, 2, 2, 2]

        # When: Выполнение функции
        result = can_partition(v)

        # Then: Проверка результата
        self.assertEqual(result, 0)

    def test_partition_not_possible(self):
        # Given: Подготовка данных
        v = [1, 2, 3, 4]

        # When: Выполнение функции
        result = can_partition(v)

        # Then: Проверка результата
        self.assertEqual(result, 0)

    def test_large_numbers(self):
        # Given: Подготовка данных
        v = [7, 3, 2, 5, 12, 5]

        # When: Выполнение функции
        result = can_partition(v)

        # Then: Проверка результата
        self.assertEqual(result, 0)

    def test_edge_cases(self):
        # Given: Подготовка данных
        v = [1, 1, 1]

        # When: Выполнение функции
        result = can_partition(v)

        # Then: Проверка результата
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
import unittest
from lab1.task10.src.task10 import can_eat_apples


class TestCanEatApples(unittest.TestCase):

    def test_basic_case(self):
        # Given: Подготовка данных
        n = 3
        s = 5
        apples = [(2, 5), (1, 1), (3, 3)]

        # When: Выполнение функции
        result = can_eat_apples(n, s, apples)

        # Then: Проверка результата
        self.assertEqual(result, '2 1 3')

    def test_not_enough_height(self):
        # Given: Подготовка данных
        n = 2
        s = 2
        apples = [(1, 2), (3, 4)]

        # When: Выполнение функции
        result = can_eat_apples(n, s, apples)

        # Then: Проверка результата
        self.assertEqual(result, -1)

    def test_all_heights_decrease(self):
        # Given: Подготовка данных
        n = 3
        s = 7
        apples = [(3, 4), (2, 1), (5, 6)]

        # When: Выполнение функции
        result = can_eat_apples(n, s, apples)

        # Then: Проверка результата
        self.assertEqual(result, '2 1 3')

    def test_height_zero_case(self):
        # Given: Подготовка данных
        n = 2
        s = 0
        apples = [(1, 2), (2, 3)]

        # When: Выполнение функции
        result = can_eat_apples(n, s, apples)

        # Then: Проверка результата
        self.assertEqual(result, -1)

    def test_immediate_failure(self):
        # Given: Подготовка данных
        n = 2
        s = 1
        apples = [(2, 3), (3, 4)]

        # When: Выполнение функции
        result = can_eat_apples(n, s, apples)

        # Then: Проверка результата
        self.assertEqual(result, -1)

    def test_edge_case_empty_apples(self):
        # Given: Подготовка данных
        n = 0
        s = 5
        apples = []

        # When: Выполнение функции
        result = can_eat_apples(n, s, apples)

        # Then: Проверка результата
        self.assertEqual(result, '')

    def test_sufficient_height(self):
        # Given: Подготовка данных
        n = 5
        s = 10
        apples = [(1, 2), (2, 3), (1, 1), (2, 2), (1, 0)]

        # When: Выполнение функции
        result = can_eat_apples(n, s, apples)

        # Then: Проверка результата
        self.assertEqual(result, '5 1 3 2 4')

    def test_unsorted_apples(self):
        # Given: Подготовка данных
        n = 4
        s = 8
        apples = [(3, 4), (1, 1), (5, 6), (2, 2)]

        # When: Выполнение функции
        result = can_eat_apples(n, s, apples)

        # Then: Проверка результата
        self.assertEqual(result, '2 4 1 3')

if __name__ == '__main__':
    unittest.main()
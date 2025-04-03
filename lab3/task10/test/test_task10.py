import unittest
from lab3.task10.src.task10 import bellman_ford


class TestBellmanFord(unittest.TestCase):
    def test_positive_weights(self):
        # Given: Подготовка данных
        # Graph: 1 -> 2 (10), 1 -> 3 (5), 2 -> 3 (2), 3 -> 4 (1)
        edges = [(1, 2, 10), (1, 3, 5), (2, 3, 2), (3, 4, 1)]

        # When: Выполнение функции
        result = bellman_ford(4, edges, 1)

        # Then: Проверка результата
        self.assertEqual(result, ['0', '10', '5', '6'])

    def test_negative_weights(self):
        # Given: Подготовка данных
        # Graph: 1 -> 2 (5), 1 -> 3 (10), 2 -> 3 (-4)
        edges = [(1, 2, 5), (1, 3, 10), (2, 3, -4)]

        # When: Выполнение функции
        result = bellman_ford(3, edges, 1)

        # Then: Проверка результата
        self.assertEqual(result, ['0', '5', '1'])

    def test_negative_cycle(self):
        # Given: Подготовка данных
        # Graph: 1 -> 2 (1), 2 -> 3 (1), 3 -> 2 (-3)
        edges = [(1, 2, 1), (2, 3, 1), (3, 2, -3)]

        # When: Выполнение функции
        result = bellman_ford(3, edges, 1)

        # Then: Проверка результата
        self.assertEqual(result, ['0', '-', '-'])

    def test_no_edges(self):
        # Given: Подготовка данных
        # Graph with multiple vertices but no edges
        edges = []

        # When: Выполнение функции
        result = bellman_ford(5, edges, 1)

        # Then: Проверка результата
        self.assertEqual(result, ['0', '*', '*', '*', '*'])

    def test_reachable_and_unreachable_nodes(self):
        # Given: Подготовка данных
        # Graph: 1 -> 2 (1), 1 -> 3 (2)
        edges = [(1, 2, 1), (1, 3, 2)]

        # When: Выполнение функции
        result = bellman_ford(5, edges, 1)

        # Then: Проверка результата
        self.assertEqual(result, ['0', '1', '2', '*', '*'])

if __name__ == '__main__':
    unittest.main()
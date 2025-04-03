import unittest
from lab3.task3.src.task3 import has_cycle


# Unit Test Class
class TestGraphCycleDetection(unittest.TestCase):

    def test_no_cycle(self):
        # Test graph with no cycle
        # Given: Подготовка данных
        n = 4
        edges = [(1, 2), (2, 3), (3, 4)]

        # When: Выполнение функции
        result = has_cycle(n, edges)

        # Then: Проверка результата
        self.assertEqual(result, 0)

    def test_cycle(self):
        # Test graph with a cycle
        # Given: Подготовка данных
        n = 4
        edges = [(1, 2), (2, 3), (3, 4), (4, 2)]

        # When: Выполнение функции
        result = has_cycle(n, edges)

        # Then: Проверка результата
        self.assertEqual(result, 1)

    def test_single_node(self):
        # Test graph with a single node and no edges
        # Given: Подготовка данных
        n = 1
        edges = []

        # When: Выполнение функции
        result = has_cycle(n, edges)

        # Then: Проверка результата
        self.assertEqual(result, 0)

    def test_single_node_with_self_loop(self):
        # Test graph with a single node and a self-loop (cycle)
        # Given: Подготовка данных
        n = 1
        edges = [(1, 1)]

        # When: Выполнение функции
        result = has_cycle(n, edges)

        # Then: Проверка результата
        self.assertEqual(result, 1)

    def test_two_nodes_no_cycle(self):
        # Test graph with two nodes and no cycle
        # Given: Подготовка данных
        n = 2
        edges = [(1, 2)]

        # When: Выполнение функции
        result = has_cycle(n, edges)

        # Then: Проверка результата
        self.assertEqual(result, 0)

    def test_two_nodes_with_cycle(self):
        # Test graph with two nodes and a cycle
        # Given: Подготовка данных
        n = 2
        edges = [(1, 2), (2, 1)]

        # When: Выполнение функции
        result = has_cycle(n, edges)

        # Then: Проверка результата
        self.assertEqual(result, 1)

    def test_disconnected_graph(self):
        # Test disconnected graph with no cycles
        # Given: Подготовка данных
        n = 5
        edges = [(1, 2), (3, 4)]

        # When: Выполнение функции
        result = has_cycle(n, edges)

        # Then: Проверка результата
        self.assertEqual(result, 0)

    def test_large_graph_with_cycle(self):
        # Test a large graph with a cycle
        # Given: Подготовка данных
        n = 5
        edges = [(1, 2), (2, 3), (3, 4), (4, 2)]

        # When: Выполнение функции
        result = has_cycle(n, edges)

        # Then: Проверка результата
        self.assertEqual(result, 1)

    def test_large_graph_no_cycle(self):
        # Test a large graph with no cycle
        # Given: Подготовка данных
        n = 5
        edges = [(1, 2), (2, 3), (3, 4), (4, 5)]

        # When: Выполнение функции
        result = has_cycle(n, edges)

        # Then: Проверка результата
        self.assertEqual(result, 0)


# Run the tests
if __name__ == '__main__':
    unittest.main()

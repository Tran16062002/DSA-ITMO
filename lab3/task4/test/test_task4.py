import unittest
from lab3.task4.src.task4 import topological_sort


class TestTopologicalSort(unittest.TestCase):

    def test_basic_case(self):
        # Тест 1: Пример с несколькими зависимостями
        # Given: Подготовка данных
        edges = [(1, 2), (4, 1), (3, 1)]

        # When: Выполнение функции
        result = topological_sort(4, edges)

        # Then: Проверка результата
        self.assertTrue(set(result) == {1, 2, 3, 4})
        self.assertEqual(result, [3, 4, 1, 2])

    def test_single_vertex(self):
        # Тест 2: Один узел
        # Given: Подготовка данных
        edges = []

        # When: Выполнение функции
        result = topological_sort(1, edges)

        # Then: Проверка результата
        self.assertEqual(result, [1])

    def test_no_edges(self):
        # Тест 3: Нет рёбер, просто упорядочиваем вершины по номерам
        # Given: Подготовка данных
        edges = []

        # When: Выполнение функции
        result = topological_sort(5, edges)

        # Then: Проверка результата
        self.assertEqual(set(result), {1, 2, 3, 4, 5})
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_multiple_dependencies(self):
        # Тест 4: Сложный граф с множеством зависимостей
        # Given: Подготовка данных
        edges = [(2, 1), (3, 1), (4, 3), (5, 4)]

        # When: Выполнение функции
        result = topological_sort(5, edges)

        # Then: Проверка результата
        self.assertTrue(set(result) == {1, 2, 3, 4, 5})
        self.assertTrue(result == [2, 5, 4, 3, 1] or result == [3, 2, 4, 5, 1])

    def test_more_than_one_valid_result(self):
        # Тест 5: Проверяем несколько правильных вариантов результата
        # Given: Подготовка данных
        edges = [(2, 3), (4, 3), (5, 3), (6, 3)]

        # When: Выполнение функции
        result = topological_sort(6, edges)

        # Then: Проверка результата
        self.assertTrue(set(result) == {1, 2, 3, 4, 5, 6})
        self.assertTrue(result == [1, 2, 4, 5, 6, 3] or result == [1, 4, 2, 5, 6, 3])


if __name__ == '__main__':
    unittest.main()

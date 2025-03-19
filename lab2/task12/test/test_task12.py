import unittest
from lab2.task12.src.task12 import slove_data, dfs


class TestDFSAndSolveData(unittest.TestCase):
    def test_solve_data(self):
        # Given: Подготовка данных
        data = [
            "1 2 3",
            "2 0 0",
            "3 0 0"
        ]
        expected_tree = [(0, 0), (2, 3), (0, 0), (0, 0)]

        # When: Выполнение функции
        n, tree, height, balance = slove_data(3, data)

        # Then: Проверка результата
        self.assertEqual(n, 3)
        self.assertEqual(tree, expected_tree)
        self.assertEqual(height, [-1, -1, -1, -1])  # Heights are not yet computed
        self.assertEqual(balance, [0, 0, 0, 0])

    def test_dfs_balanced_tree(self):
        # Given: Подготовка данных
        data = [
            "1 2 3",
            "2 0 0",
            "3 0 0"
        ]

        # When: Выполнение функции
        n, tree, height, balance = slove_data(3, data)
        dfs(1, tree, height, balance)

        # Then: Проверка результата
        self.assertEqual(height[1], 2)
        self.assertEqual(height[2], 1)
        self.assertEqual(height[3], 1)
        self.assertEqual(balance[1], 0)
        self.assertEqual(balance[2], 0)
        self.assertEqual(balance[3], 0)

    def test_dfs_unbalanced_tree(self):
        # Given: Подготовка данных
        data = [
            "1 2 0",
            "2 3 0",
            "3 0 0"
        ]

        # When: Выполнение функции
        n, tree, height, balance = slove_data(3, data)
        dfs(1, tree, height, balance)

        # Then: Проверка результата
        self.assertEqual(height[1], 3)
        self.assertEqual(height[2], 2)
        self.assertEqual(height[3], 1)
        self.assertEqual(balance[1], -2)
        self.assertEqual(balance[2], -1)
        self.assertEqual(balance[3], 0)

    def test_empty_tree(self):
        n, tree, height, balance = slove_data(0, [])
        self.assertEqual(n, 0)
        self.assertEqual(tree, [])
        self.assertEqual(height, [])
        self.assertEqual(balance, [])


if __name__ == "__main__":
    unittest.main()

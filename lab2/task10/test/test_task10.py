import unittest
from lab2.task10.src.task10 import find_tree, is_bst


class TestFindTree(unittest.TestCase):
    def test_find_tree(self):
        # Given: Подготовка данных
        data = [
            "2 1 3",
            "1 0 0",
            "3 0 0"
        ]
        expected_tree = [(2, 0, 2), (1, -1, -1), (3, -1, -1)]

        # When: Выполнение функции
        rresult = find_tree(data)

        # Then: Проверка результата
        self.assertEqual(rresult, expected_tree)

    def test_is_bst_valid(self):
        tree = [(2, 0, 2), (1, -1, -1), (3, -1, -1)]
        self.assertFalse(is_bst(tree))

    def test_is_bst_invalid(self):
        tree = [(2, 1, 2), (3, -1, -1), (1, -1, -1)]  # Not a BST
        self.assertFalse(is_bst(tree))

    def test_is_bst_empty(self):
        self.assertTrue(is_bst([]))  # Empty tree should be valid

    def test_is_bst_single_node(self):
        tree = [(5, -1, -1)]
        self.assertTrue(is_bst(tree))


if __name__ == "__main__":
    unittest.main()

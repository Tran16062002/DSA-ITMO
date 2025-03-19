import unittest
from lab2.task5.src.task5 import process_operations, BST


class TestBST(unittest.TestCase):
    def setUp(self):
        self.tree = BST()

    def test_insert_and_exists(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(8)

        self.assertTrue(self.tree.exists(5))
        self.assertTrue(self.tree.exists(3))
        self.assertTrue(self.tree.exists(8))
        self.assertFalse(self.tree.exists(10))

    def test_delete(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(8)

        self.tree.delete(3)
        self.assertFalse(self.tree.exists(3))
        self.assertTrue(self.tree.exists(5))
        self.assertTrue(self.tree.exists(8))

    def test_next(self):
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(8)

        self.assertEqual(self.tree.next(2), 5)
        self.assertEqual(self.tree.next(5), 8)
        self.assertEqual(self.tree.next(8), "none")

    def test_prev(self):
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(8)

        self.assertEqual(self.tree.prev(8), 5)
        self.assertEqual(self.tree.prev(5), 2)
        self.assertEqual(self.tree.prev(2), "none")

    def test_process_operations(self):
        # Given: Подготовка данных
        operations = [
            "insert 5",
            "insert 3",
            "insert 8",
            "exists 5",
            "exists 10",
            "next 3",
            "prev 8",
            "delete 3",
            "exists 3"
        ]
        expected_output = ["true", "false", "5", "5", "false"]

        # When: Выполнение функции
        result = process_operations(operations)

        # Then: Проверка результата
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()

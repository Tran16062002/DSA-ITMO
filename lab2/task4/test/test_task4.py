import unittest
import random
from lab2.task4.src.task4 import insert, merge, get_size, find, kth_element, split


class TestTreap(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        self.root = None

    def test_insert_and_find(self):
        keys = [5, 3, 8, 1, 4, 7, 10]
        for key in keys:
            self.root = insert(self.root, key)

        for key in keys:
            self.assertTrue(find(self.root, key))
        self.assertFalse(find(self.root, 2))
        self.assertFalse(find(self.root, 9))

    def test_split(self):
        keys = [5, 3, 8, 1, 4, 7, 10]
        for key in keys:
            self.root = insert(self.root, key)

        left, right = split(self.root, 6)
        self.assertFalse(find(right, 5))
        self.assertTrue(find(right, 7))

    def test_merge(self):
        left = insert(None, 1)
        left = insert(left, 2)
        right = insert(None, 3)
        right = insert(right, 4)
        merged_root = merge(left, right)

        for key in [1, 2, 3, 4]:
            self.assertTrue(find(merged_root, key))

    def test_kth_element(self):
        keys = [5, 3, 8, 1, 4, 7, 10]
        for key in keys:
            self.root = insert(self.root, key)

        sorted_keys = sorted(keys)
        for k in range(1, len(keys) + 1):
            self.assertEqual(kth_element(self.root, k), sorted_keys[k - 1])


if __name__ == "__main__":
    unittest.main()

import unittest
from lab2.task14.src.task14 import AVLTree, Node


class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_insert_single_node(self):
        self.tree.root = self.tree.insert(self.tree.root, 10)
        self.assertEqual(self.tree.root.key, 10)
        self.assertEqual(self.tree.root.height, 1)

    def test_insert_multiple_nodes(self):
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            self.tree.root = self.tree.insert(self.tree.root, key)
        self.assertEqual(self.tree.root.key, 30)  # AVL balancing should place 30 as root
        self.assertEqual(self.tree.root.height, 3)

    def test_balance_factor(self):
        self.tree.root = self.tree.insert(self.tree.root, 10)
        self.tree.root = self.tree.insert(self.tree.root, 20)
        self.tree.root = self.tree.insert(self.tree.root, 30)
        self.assertEqual(self.tree.balance_factor(self.tree.root), 0)  # Balanced AVL tree

    def test_rotate_left(self):
        root = Node(10, None, Node(20))
        new_root = self.tree.rotate_left(root)
        self.assertEqual(new_root.key, 20)
        self.assertEqual(new_root.left.key, 10)

    def test_rotate_right(self):
        root = Node(20, Node(10), None)
        new_root = self.tree.rotate_right(root)
        self.assertEqual(new_root.key, 10)
        self.assertEqual(new_root.right.key, 20)

    def test_build_tree(self):
        nodes_info = [(30, 2, 3), (20, 0, 0), (40, 0, 0)]
        self.tree.build_tree(nodes_info)
        self.assertEqual(self.tree.root.key, 30)
        self.assertEqual(self.tree.root.left.key, 20)
        self.assertEqual(self.tree.root.right.key, 40)

    def test_generate_tree_output(self):
        nodes_info = [(30, 2, 3), (20, 0, 0), (40, 0, 0)]
        self.tree.build_tree(nodes_info)
        output = self.tree.generate_tree_output()
        expected_output = ["3", "30 2 3", "20 0 0", "40 0 0"]
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()

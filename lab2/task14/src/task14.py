import psutil
import os
from time import perf_counter
from lab2.utils import read_file, write_file

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        self.nodes = {}
        self.index_map = {}
        self.index_counter = 1

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def fix_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.fix_height(node)
        self.fix_height(new_root)
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.fix_height(node)
        self.fix_height(new_root)
        return new_root

    def balance(self, node):
        self.fix_height(node)
        if self.balance_factor(node) == 2:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if self.balance_factor(node) == -2:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, node, key):
        if not node:
            new_node = Node(key)
            self.nodes[len(self.nodes) + 1] = new_node  # Добавляем в nodes
            return new_node
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        return self.balance(node)

    def build_tree(self, nodes_info):
        self.nodes = {i + 1: Node(k) for i, (k, _, _) in enumerate(nodes_info)}
        for i, (k, l, r) in enumerate(nodes_info):
            if l:
                self.nodes[i + 1].left = self.nodes[l]
            if r:
                self.nodes[i + 1].right = self.nodes[r]
        self.root = self.nodes[1] if self.nodes else None

    def update_nodes(self, node):
        if not node:
            return
        if node not in self.index_map:
            self.index_map[node] = self.index_counter
            self.nodes[self.index_counter] = node  # Обновляем nodes
            self.index_counter += 1
        self.update_nodes(node.left)
        self.update_nodes(node.right)

    def generate_tree_output(self):
        self.index_map.clear()
        self.index_counter = 1
        self.nodes.clear()
        self.update_nodes(self.root)
        output = [f"{len(self.nodes)}"]
        for i in sorted(self.nodes):
            node = self.nodes[i]
            left_index = self.index_map.get(node.left, 0)
            right_index = self.index_map.get(node.right, 0)
            output.append(f"{node.key} {left_index} {right_index}")
        return output


def task14():
    process = psutil.Process(os.getpid())
    t1_start = perf_counter()
    start_memory = process.memory_info().rss / 1024 / 1024
    data = read_file(PATH_INPUT)

    n = int(data[0])
    nodes_info = [tuple(map(int, line.split())) for line in data[1:n+1]]
    x = int(data[n + 1])

    avl = AVLTree()
    avl.build_tree(nodes_info)
    avl.root = avl.insert(avl.root, x)
    result = avl.generate_tree_output()

    write_file(PATH_OUTPUT, str("\n".join(result) + "\n"))

    t1_stop = perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024
    print('Время работы: %s секунд ' % (t1_stop - t1_start))
    print(f"память использовать: {end_memory - start_memory:.6f} MB")

if __name__ == '__main__':
    task14()



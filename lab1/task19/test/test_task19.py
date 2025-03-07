import unittest
from lab1.task19.src.task19 import matrix_chain_order,optimal_parenthesis


class TestMatrixChainMultiplication(unittest.TestCase):

    def test_matrix_chain_order(self):
        # Given: Подготовка данных
        p = [10, 20, 30, 40, 30]

        # When: Выполнение функции
        m, s = matrix_chain_order(p)

        # Then: Проверка результата
        self.assertEqual(m[0][3], 30000)
        self.assertEqual(s[0][3], 2)

    def test_optimal_parenthesis(self):
        # Given: Подготовка данных
        p = [10, 20, 30, 40, 30]

        # When: Выполнение функции
        m, s = matrix_chain_order(p)
        optimal_str = optimal_parenthesis(s, 0, len(p) - 2)

        # Then: Проверка результата
        self.assertEqual(optimal_str, "(((AA)A)A)")

    def test_edge_case_single_matrix(self):
        # Given: Подготовка данных
        p = [10, 20]

        # When: Выполнение функции
        m, s = matrix_chain_order(p)
        optimal_str = optimal_parenthesis(s, 0, 0)

        # Then: Проверка результата
        self.assertEqual(m[0][0], 0)
        self.assertEqual(optimal_str, "A")

if __name__ == '__main__':
    unittest.main()
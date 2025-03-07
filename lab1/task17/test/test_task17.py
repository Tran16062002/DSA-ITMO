import unittest
from lab1.task17.src.task17 import knight_dialer

MOD = 10 ** 9

moves = {
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
    0: [4, 6]
}



class TestKnightDialer(unittest.TestCase):

    def test_case_1(self):
        # Given: Подготовка данных
        N = 1

        # When: Выполнение функции
        result = knight_dialer(N)

        # Then: Проверка результата
        self.assertEqual(result, 8)

    def test_case_2(self):
        # Given: Подготовка данных
        N = 2

        # When: Выполнение функции
        result = knight_dialer(N)

        # Then: Проверка результата
        self.assertEqual(result, 16)

    def test_case_3(self):
        # Given: Подготовка данных
        N = 3

        # When: Выполнение функции
        result = knight_dialer(N)

        # Then: Проверка результата
        self.assertEqual(result, 36)

    def test_case_4(self):
        # Given: Подготовка данных
        N = 4

        # When: Выполнение функции
        result = knight_dialer(N)

        # Then: Проверка результата
        self.assertEqual(result, 82)

    def test_case_5(self):
        # Given: Подготовка данных
        N = 5

        # When: Выполнение функции
        result = knight_dialer(N)

        # Then: Проверка результата
        self.assertEqual(result, 188)

    def test_case_6(self):
        # Testing with a larger N for performance
        # Given: Подготовка данных
        N = 50

        # When: Выполнение функции
        result = knight_dialer(N)

        # Then: Проверка результата
        self.assertEqual(result, 549298688)


if __name__ == '__main__':
    unittest.main()
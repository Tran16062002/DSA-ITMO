import unittest
from lab3.task14.src.task14 import min_time_to_reach_villages


class TestMinTimeToReachVillages(unittest.TestCase):

    def test_basic_case(self):
        # Given: Подготовка данных
        N = 3
        d = 1
        v = 3
        R = 2
        trips = [
            (1, 0, 2, 5),
            (2, 6, 3, 10)
        ]

        # When: Выполнение функции
        result = min_time_to_reach_villages(N, d, v, R, trips)

        # Then: Проверка результата
        self.assertEqual(result, 10)

    def test_no_possible_route(self):
        # Given: Подготовка данных
        N = 3
        d = 1
        v = 3
        R = 1
        trips = [
            (1, 0, 2, 5)  # No route to village 3
        ]

        # When: Выполнение функции
        result = min_time_to_reach_villages(N, d, v, R, trips)

        # Then: Проверка результата
        self.assertEqual(result, -1)

    def test_multiple_paths(self):
        # Given: Подготовка данных
        N = 4
        d = 1
        v = 4
        R = 3
        trips = [
            (1, 0, 2, 5),
            (2, 6, 3, 10),
            (1, 0, 3, 8),
            (3, 9, 4, 12)
        ]

        # When: Выполнение функции
        result = min_time_to_reach_villages(N, d, v, R, trips)

        # Then: Проверка результата
        # The shortest path should be 1 -> 3 -> 4 with total time 12
        self.assertEqual(result, 12)

    def test_delayed_departure(self):
        # Given: Подготовка данных
        N = 3
        d = 1
        v = 3
        R = 2
        trips = [
            (1, 5, 2, 10),
            (2, 15, 3, 20)
        ]

        # When: Выполнение функции
        result = min_time_to_reach_villages(N, d, v, R, trips)

        # Then: Проверка результата
        # The function must wait for the first bus at t=5
        self.assertEqual(result, 20)

    def test_circular_routes(self):
        # Given: Подготовка данных
        N = 3
        d = 1
        v = 3
        R = 3
        trips = [
            (1, 0, 2, 5),
            (2, 6, 1, 8),  # Circular route back to 1
            (2, 7, 3, 12)
        ]

        # When: Выполнение функции
        result = min_time_to_reach_villages(N, d, v, R, trips)

        # Then: Проверка результата
        # The shortest path should be 1 -> 2 -> 3 with total time 12
        self.assertEqual(result, 12)

    def test_large_case(self):
        # Given: Подготовка данных
        N = 1000
        d = 1
        v = 1000
        R = 999
        trips = [(i, i * 2, i + 1, (i + 1) * 2) for i in range(1, 1000)]

        # When: Выполнение функции
        result = min_time_to_reach_villages(N, d, v, R, trips)

        # Then: Проверка результата
        # The expected shortest time should be 2000 (sum of all edges)
        self.assertEqual(result, 2000)


if __name__ == '__main__':
    unittest.main()

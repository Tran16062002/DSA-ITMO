import unittest
from lab1.task2.src.task2 import min_refills


class TestMinRefills(unittest.TestCase):

    def test_no_refills_needed(self):
        # Given: Подготовка данных
        d = 100
        m = 100
        stops = []

        # When: Выполнение функции
        result = min_refills(d, m, stops)

        # Then: Проверка результата
        self.assertEqual(result, 0)

    def test_one_refill_needed(self):
        # Given: Подготовка данных
        d = 100
        m = 50
        stops = [50]

        # When: Выполнение функции
        result = min_refills(d, m, stops)

        # Then: Проверка результата
        self.assertEqual(result, 1)

    def test_two_refills_needed(self):
        # Given: Подготовка данных
        d = 200
        m = 100
        stops = [50, 150]

        # When: Выполнение функции
        result = min_refills(d, m, stops)

        # Then: Проверка результата
        self.assertEqual(result, 2)

    def test_impossible_trip(self):
        # Given: Подготовка данных
        d = 200
        m = 100
        stops = [90, 150]

        # When: Выполнение функции
        result = min_refills(d, m, stops)

        # Then: Проверка результата
        self.assertEqual(result, 2)

    def test_no_stops(self):
        # Given: Подготовка данных
        d = 300
        m = 100
        stops = []

        # When: Выполнение функции
        result = min_refills(d, m, stops)

        # Then: Проверка результата
        self.assertEqual(result, -1)

    def test_multiple_stops(self):
        # Given: Подготовка данных
        d = 400
        m = 200
        stops = [100, 200, 300]

        # When: Выполнение функции
        result = min_refills(d, m, stops)

        # Then: Проверка результата
        self.assertEqual(result, 1)

    def test_edge_case_refill_stations_at_max_distance(self):
        # Given: Подготовка данных
        d = 400
        m = 200
        stops = [200]

        # When: Выполнение функции
        result = min_refills(d, m, stops)

        # Then: Проверка результата
        self.assertEqual(result, 1)

    def test_large_distance(self):
        # Given: Подготовка данных
        d = 1000
        m = 300
        stops = [200, 400, 600, 800]

        # When: Выполнение функции
        result = min_refills(d, m, stops)

        # Then: Проверка результата
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
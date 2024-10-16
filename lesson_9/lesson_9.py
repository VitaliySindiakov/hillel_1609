import unittest

from lesson_7.lesson_7 import sum_of_two, arithmetic_mean, get_cars_by_criteria


class MyTest(unittest.TestCase):
    def test_sum_of_two(self):
        expected_result = sum_of_two(3, 2)
        self.assertEqual(expected_result, 5)

    def test_sum_of_two_negative_value(self):
        expected_result = sum_of_two(-3, -2)
        self.assertNotEqual(expected_result, 5)

    def test_sum_of_two_error(self):
        with self.assertRaises(TypeError):
            sum_of_two(5, "2")

    def test_arithmetic_mean(self):
        lst1 = [1, 2, 3, 4, 5]
        self.assertEqual(arithmetic_mean(lst1), 3)

    def test_arithmetic_mean_neg_value(self):
        lst1 = [-1, -2, -3, -4, -5]
        self.assertEqual(arithmetic_mean(lst1), -3)

    def test_arithmetic_error(self):
        lst1 = ['1', 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            arithmetic_mean(lst1, 3)

    def test_get_car(self):
        expected_result: dict = {'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000),
                                 'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000)}
        actual_result = get_cars_by_criteria((2017, 1.6, 36000))
        self.assertEqual(actual_result, expected_result)

    def test_get_car_neg_1(self):
        expected_result: dict = {'Audi': ('black', 2020, 2.0, 'sedan', 55000),
                                 'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000)}
        actual_result = get_cars_by_criteria((2017, 1.6, 36000))
        self.assertNotEqual(actual_result, expected_result)

    def test_get_car_neg_2_out_of_criteria(self):
        actual_result = get_cars_by_criteria((2025, 2, 500))
        self.assertFalse(actual_result)

    def test_get_car_error(self):
        with self.assertRaises(ValueError):
            get_cars_by_criteria((2017, 1.6))


if __name__ == '__main__':
    unittest.main()

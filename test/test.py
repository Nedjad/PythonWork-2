import unittest
from unittest.mock import patch
from task import AverageComparator, get_list_from_input

class TestAverageComparator(unittest.TestCase):

    @patch('builtins.input', side_effect=["10 20 30", "1 2 3"])
    def test_first_list_greater(self, mock_input):
        list1 = get_list_from_input("Введите числа для первого списка, разделенные пробелом: ")
        list2 = get_list_from_input("Введите числа для второго списка, разделенные пробелом: ")
        comparator = AverageComparator(list1, list2)
        self.assertEqual(comparator.compare_averages(), "Первый список имеет большее среднее значение")

    @patch('builtins.input', side_effect=["1 2 3", "10 20 30"])
    def test_second_list_greater(self, mock_input):
        list1 = get_list_from_input("Введите числа для первого списка, разделенные пробелом: ")
        list2 = get_list_from_input("Введите числа для второго списка, разделенные пробелом: ")
        comparator = AverageComparator(list1, list2)
        self.assertEqual(comparator.compare_averages(), "Второй список имеет большее среднее значение")

    @patch('builtins.input', side_effect=["1 2 3", "1 2 3"])
    def test_averages_equal(self, mock_input):
        list1 = get_list_from_input("Введите числа для первого списка, разделенные пробелом: ")
        list2 = get_list_from_input("Введите числа для второго списка, разделенные пробелом: ")
        comparator = AverageComparator(list1, list2)
        self.assertEqual(comparator.compare_averages(), "Средние значения равны")

if __name__ == '__main__':
    unittest.main()

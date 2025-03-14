import unittest
from algorithms.bubbleSort import bubbleSort
from algorithms.insertionSort import insertionSort
from algorithms.mergeSort import mergeSort
from algorithms.quickSort import quickSort

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        """Runs before every test"""
        self.test_cases = [
            ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
            ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
            ([3, 0, -2, 5, 10, -3], [-3, -2, 0, 3, 5, 10]),
            ([1], [1]),
            ([], [])
        ]

    def test_bubble_sort(self):
        """Tests for bubble sort"""
        for input_arr, expected in self.test_cases:
            self.assertEqual(bubbleSort(input_arr[:]), expected)

    def test_insertion_sort(self):
        """Tests for insertion sort"""
        for input_arr, expected in self.test_cases:
            self.assertEqual(insertionSort(input_arr[:]), expected)

    def test_merge_sort(self):
        """Tests for merge sort"""
        for input_arr, expected in self.test_cases:
            self.assertEqual(mergeSort(input_arr[:]), expected)

    def test_quick_sort(self):
        """Tests for quick sort"""
        for input_arr, expected in self.test_cases:
            self.assertEqual(quickSort(input_arr[:]), expected)

if __name__ == '__main__':
    unittest.main()

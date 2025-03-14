import unittest
from data_generator.generator import randomList

class test_data_generator(unittest.TestCase):
    def test_random_list_size(self):
        """Test if randomList generates the correct number of elements."""
        size = 25
        result = randomList(size)
        self.assertEqual(len(result), size)

    def test_random_list_range(self):
        """Test if randomList generates values within the specified range."""
        size = 21
        limit = 500
        result = randomList(size, limit)
        self.assertTrue(all(0 <= num <= limit for num in result))


if __name__ == '__main__':
    unittest.main()

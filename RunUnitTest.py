import unittest

def add(x, y):
    return x + y    


class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)    

    def test_add_positive_and_negative_numbers(self):
        result = add(-2, 3)
        self.assertEqual(result, 1) 

    def test_add_zero_and_positive_numbers(self):
        result = add(0, 3)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()



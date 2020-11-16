import unittest

from wedd import wedd


class WeddTestCase(unittest.TestCase):
    def test1(self):
        edges = [[1, 2], [2, 4], [3, 5]]
        self.assertEqual(wedd(edges), 4)

    def test2(self):
        edges = [[1, 2], [2, 4], [1, 3], [3, 5], [8, 10]]
        self.assertEqual(wedd(edges), 6)

    def test_one_pair(self):
        edges = [[1, 2]]
        self.assertEqual(wedd(edges), 0)

    def test_one_tribe(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        self.assertEqual(wedd(edges), 0)

    def test_only_boys(self):
        edges = [[1, 3], [5, 7], [9, 11]]
        self.assertEqual(wedd(edges), 0)

    def test_only_girls(self):
        edges = [[2, 4], [6, 8], [10, 12]]
        self.assertEqual(wedd(edges), 0)


if __name__ == '__main__':
    unittest.main()

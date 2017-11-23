import unittest

from search.k_closet_points_heap import k_closet_points

class KClosetPointsTestCase(unittest.TestCase):
    # def test_case1(self):
    #    l = [0, 1, 2, 3, 4, 5]
    #    self.assertEqual(k_closet_points(l, 3), [0, 1, 2])

    def test_case2(self):
        l = [(0, 0), (1, 1), (2, 2), (3, 3)]
        self.assertEqual(set(k_closet_points(l, 3)), set([(0, 0), (1, 1), (2, 2)]))

if __name__ == '__main__':
    unittest.main()

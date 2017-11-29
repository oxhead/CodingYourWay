import unittest

from tree.path_sum import Solution
from utils.tree import parse_tree, print_tree

class PathSumTestCase(unittest.TestCase):
    def test_case1(self):
        input_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        root = parse_tree(input_list)
        print_tree(root)
        self.assertTrue(Solution().hasPathSum(root, 22))

if __name__ == '__main__':
    unittest.main()

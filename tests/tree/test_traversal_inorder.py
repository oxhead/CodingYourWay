import unittest

from tree.traversal_inorder import Solution
from utils.tree import parse_tree, print_tree

class TraversalInorderTestCase(unittest.TestCase):
    def test_case1(self):
        input_list = [1, None, 2, 3]
        root = parse_tree(input_list)
        print_tree(root, kind='inorder')
        solution = Solution()
        result = solution.inorderTraversal(root)
        self.assertEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()

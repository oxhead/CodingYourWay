"""
https://leetcode.com/problems/merge-two-binary-trees

Related:
"""

"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

Note: The merging process must start from the root nodes of both trees.
"""

from utils import parse_tree, serialize_tree

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Time: O(n)
        # Space: O(h)
        if not t1 and not t2: return None
        elif not t2: return t1
        elif not t1: return t2
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


if __name__ == '__main__':
    test_cases = [
        (([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7]), [3, 4, 5, 5, 4, None, 7]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().mergeTrees(parse_tree(test_case[0][0]), parse_tree(test_case[0][1]))
        print('output:', serialize_tree(output))
        assert serialize_tree(output) == test_case[1]


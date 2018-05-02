"""
https://leetcode.com/problems/construct-string-from-binary-tree/description/

Related:
  - lt_536_construct-binary-tree-from-string
  - lt_652_find-duplicate-subtrees
"""

"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".

Example 2:

Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""

from utils import parse_tree

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        elif t.left and t.right:
            return str(t.val) + "({})({})".format(self.tree2str(t.left), self.tree2str(t.right))
        elif t.left:
            return str(t.val) + "({})".format(self.tree2str(t.left))
        elif t.right:
            return str(t.val) + "()({})".format(self.tree2str(t.right))
        else:
            return str(t.val)


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4], "1(2(4))(3)"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().tree2str(parse_tree(test_case[0]))
        print('output:', output)
        assert output == test_case[1]


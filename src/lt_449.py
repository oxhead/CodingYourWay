"""
https://leetcode.com/problems/serialize-and-deserialize-bst

Related:
  - lt_297_serialize-and-deserialize-binary-tree
  - lt_652_find-duplicate-subtrees
"""

"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

from base import TreeNode
from utils import parse_tree, serialize_tree, is_bst_equal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Time: O(n)
        # Space: O(?)
        queue = [root]
        output = []
        while queue:
            node = queue.pop(0)
            output.append(str(node.val) if node else "None")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        i = len(output) - 1
        while i >= 0:
            if output[i] != "None": break
            i -= 1
        return "#".join(output[:i+1])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Time: O(n)
        # Space: O(n)
        if not data: return None
        nodes = [TreeNode(int(n)) if n != "None" else None for n in data.split('#')]
        children = nodes[::-1]
        root = children.pop()
        for node in nodes:
            if node:
                if children: node.left = children.pop()
                if children: node.right = children.pop()
        return root
 

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == '__main__':
    test_cases = [
        ([], None),
        ([2, 1, 3], None),
        ([1, 2, 3], None),
        ([10, 5, 15, None, None, 6, 20], None),
        ([3, 1, 5, 0, 2, 4, 6], None),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        codec = Codec()
        root = parse_tree(test_case[0])
        output = codec.deserialize(codec.serialize(root))
        print('input:', serialize_tree(root))
        print('output:', serialize_tree(output))
        assert is_bst_equal(root, output)


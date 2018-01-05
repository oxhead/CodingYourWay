class ListNode:
    def __init__(self, value):
        self.value = value
        self._next = None
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, node):
        self._next = node


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

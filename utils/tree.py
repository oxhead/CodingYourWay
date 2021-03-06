from base import TreeNode

def parse_tree(input_list):
    """
    https://discuss.leetcode.com/topic/16600/tree-deserializer-and-visualizer-for-python
    """
    nodes = [TreeNode(n) if n is not None else None for n in input_list]
    children = nodes[::-1]
    root = children.pop()
    for node in nodes:
        if node:
            if children: node.left = children.pop()
            if children: node.right = children.pop()
    return root

def print_tree(root, kind='inorder'):
    if kind == 'inorder':
        print_tree_inorder(root)

def print_tree_inorder(root):
    if not root:
        return
    print(root.val)
    print_tree_inorder(root.left)
    print_tree_inorder(root.right)

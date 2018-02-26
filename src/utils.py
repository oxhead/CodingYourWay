from base import ListNode, TreeNode

def to_linked_list(numbers):
    head = ListNode('#')
    ptr = head
    for n in numbers:
        ptr.next = ListNode(n)
        ptr = ptr.next

    return head.next


def to_list(node):
    l = list()
    while node != None:
        l.append(node.val)
        node = node.next
    return l

def find_node_by_index(node, index):
    count = 0
    while node and count <= index:
        if count == index:
            return node
        count += 1
        node = node.next
    return None


def parse_tree(input_list):
    """
    https://discuss.leetcode.com/topic/16600/tree-deserializer-and-visualizer-for-python
    """
    if not input_list or len(input_list) < 1: return None
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

def is_height_balanced_bst(root):
    if not root:
        return True
    return abs(get_tree_height(root.left) - get_tree_height(root.right)) <= 1

def get_tree_height(root):
    if not root:
        return 0
    return 1 + max(get_tree_height(root.left), get_tree_height(root.right))

        


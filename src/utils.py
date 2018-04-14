from base import ListNode, RandomListNode, TreeNode
from base import NestedInteger
from base import Interval

def to_linked_list(numbers):
    head = ListNode('#')
    ptr = head
    for n in numbers:
        ptr.next = ListNode(n)
        ptr = ptr.next

    return head.next

def to_random_linked_list(numbers, random_list):
    head = RandomListNode('#')
    ptr = head
    random_node_list = []
    for n in numbers:
        ptr.next = RandomListNode(n)
        ptr = ptr.next
        random_node_list.append(ptr)

    for i, random_index in enumerate(random_list):
        random_node_list[i].random = random_node_list[random_list[i]] if random_list[i] is not None else None

    return head.next

def to_linked_list_by_pairs(lists):
    object_set = set()
    for n1, n2 in lists:
        object_set.add(n1)
        if n2:
            object_set.add(n2)
    objects = {n: ListNode(n) for n in object_set}
    for n1, n2 in lists:
        objects[n1].next = objects[n2] if n2 else None
    return objects[lists[0][0]]

def to_intersected_linked_list_by_pairs(lists, valA, valB, valIntersect):
    object_set = set()
    for n1, n2 in lists:
        object_set.add(n1)
        object_set.add(n2)
    objects = {n: ListNode(n) for n in object_set}
    for n1, n2 in lists:
        objects[n1].next = objects[n2]
    return objects[valA], objects[valB], objects[valIntersect] if valIntersect else None

def to_list(node):
    l = list()
    while node != None:
        l.append(node.val)
        node = node.next
    return l

def to_random_list(node):
    l = list()
    n = node
    while n != None:
        l.append(n.label)
        n = n.next

    r = list()
    n = node
    while n != None:
        r.append(n.random.label if n.random else None)
        n = n.next
    return l, r

def find_node_by_index(node, index):
    count = 0
    while node and count <= index:
        if count == index:
            return node
        count += 1
        node = node.next
    return None


def parse_tree(input_list, return_nodes=False):
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
    if return_nodes:
        return root, nodes
    else:
        return root

def serialize_tree(root):
    output = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            output.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            output.append(None)
    i = len(output) - 1
    while i >= 0:
        if output[i] != None:
            return output[:i+1]
        i -= 1
    return output[:i]


def search_node_by_value(nodes, val):
    for node in nodes:
        if node and node.val == val: return node
    return None


def print_tree(root, kind='inorder'):
    if kind == 'inorder':
        print_tree_inorder(root)


def print_tree_inorder(root):
    if not root:
        return
    print_tree_inorder(root.left)
    print(root.val)
    print_tree_inorder(root.right)

def tree_traversal_inorder(root):
    def _traversal(node):
        if not node: return
        _traversal(node.left)
        output.append(node.val)
        _traversal(node.right)
    output = []
    _traversal(root)
    return output

def is_height_balanced_bst(root):
    if not root:
        return True
    return abs(get_tree_height(root.left) - get_tree_height(root.right)) <= 1

def get_tree_height(root):
    if not root:
        return 0
    return 1 + max(get_tree_height(root.left), get_tree_height(root.right))

def is_bst_equal(root1, root2):
    if root1 and not root2: return False
    if not root1 and root2: return False
    if not root1 and not root2: return True
    if root1.val != root2.val: return False
    return is_bst_equal(root1.left, root2.left) and is_bst_equal(root1.right, root2.right)

def to_nested_list(data):
    return [NestedInteger(d) for d in data]

def to_interval_list(interval_list):
    return [Interval(*interval) for interval in interval_list]

def is_interval_equal(il1, il2):
    l1 = [(interval.start, interval.end) for interval in il1]
    l2 = [(interval.start, interval.end) for interval in il2]
    return sorted(l1) == sorted(l2)

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

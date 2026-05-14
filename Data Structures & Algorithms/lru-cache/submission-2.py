class Node():
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            node.next = self.head
            if self.head:
                self.head.prev = node
            self.head = node
            if self.tail is None:       # first insert
                self.tail = node
            if len(self.cache) > self.capacity:
                lru = self.tail
                self.tail = lru.prev
                if self.tail:
                    self.tail.next = None
                del self.cache[lru.key]

    def _move_to_head(self, node):
        if node is self.head:
            return
        prev, next = node.prev, node.next
        if prev: prev.next = next
        if next: next.prev = prev
        if node is self.tail:           # moving tail up
            self.tail = prev
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
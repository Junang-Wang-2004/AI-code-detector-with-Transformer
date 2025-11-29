class LRUCache:
    class Node:
        def __init__(self, k, v):
            self.key = k
            self.val = v
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.node_map = {}
        self.sentinel_head = self.Node(0, 0)
        self.sentinel_tail = self.Node(0, 0)
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head

    def _detach(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _attach(self, node):
        node.next = self.sentinel_head.next
        node.prev = self.sentinel_head
        self.sentinel_head.next.prev = node
        self.sentinel_head.next = node

    def _evict(self):
        lru = self.sentinel_head.next
        self._detach(lru)
        del self.node_map[lru.key]

    def get(self, key):
        if key in self.node_map:
            node = self.node_map[key]
            self._detach(node)
            self._attach(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self._detach(node)
            self._attach(node)
        else:
            if len(self.node_map) == self.capacity:
                self._evict()
            new_node = self.Node(key, value)
            self._attach(new_node)
            self.node_map[key] = new_node

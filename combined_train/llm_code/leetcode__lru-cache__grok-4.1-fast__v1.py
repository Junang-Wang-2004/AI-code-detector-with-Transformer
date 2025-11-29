class C1:

    class Node:

        def __init__(self, a1, a2):
            self.key = a1
            self.val = a2
            self.prev = None
            self.next = None

    def __init__(self, a1):
        self.capacity = a1
        self.node_map = {}
        self.sentinel_head = self.Node(0, 0)
        self.sentinel_tail = self.Node(0, 0)
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head

    def _detach(self, a1):
        a1.prev.next = a1.next
        a1.next.prev = a1.prev

    def _attach(self, a1):
        a1.next = self.sentinel_head.next
        a1.prev = self.sentinel_head
        self.sentinel_head.next.prev = a1
        self.sentinel_head.next = a1

    def _evict(self):
        v1 = self.sentinel_head.next
        self._detach(v1)
        del self.node_map[v1.key]

    def get(self, a1):
        if a1 in self.node_map:
            v1 = self.node_map[a1]
            self._detach(v1)
            self._attach(v1)
            return v1.val
        return -1

    def put(self, a1, a2):
        if a1 in self.node_map:
            v1 = self.node_map[a1]
            v1.val = a2
            self._detach(v1)
            self._attach(v1)
        else:
            if len(self.node_map) == self.capacity:
                self._evict()
            v2 = self.Node(a1, a2)
            self._attach(v2)
            self.node_map[a1] = v2

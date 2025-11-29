import random
v1 = 32

class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = [None] * v1

class C2:

    def __init__(self):
        self._sentinel = C1(-float('inf'))
        self._length = 0

    def _locate_predecessors(self, a1):
        v1 = [None] * v1
        v2 = self._sentinel
        for v3 in range(v1 - 1, -1, -1):
            while v2.next[v3] is not None and v2.next[v3].val < a1:
                v2 = v2.next[v3]
            v1[v3] = v2
        return v1

    def _random_height(self):
        v1 = 1
        while v1 < v1 and random.randint(1, 2) == 1:
            v1 += 1
        return v1

    def search(self, a1):
        v1 = self._locate_predecessors(a1)
        v2 = v1[0].next[0]
        return v2 is not None and v2.val == a1

    def add(self, a1):
        v1 = self._random_height()
        v2 = self._locate_predecessors(a1)
        v3 = C1(a1)
        for v4 in range(v1):
            v3.next[v4] = v2[v4].next[v4]
            v2[v4].next[v4] = v3
        self._length += 1

    def erase(self, a1):
        v1 = self._locate_predecessors(a1)
        v2 = v1[0].next[0]
        if v2 is None or v2.val != a1:
            return False
        for v3 in range(v1):
            if v1[v3].next[v3] == v2:
                v1[v3].next[v3] = v2.next[v3]
        self._length -= 1
        return True

    def __len__(self):
        return self._length

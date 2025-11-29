class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None
        self.prev = None

class C2:

    def __init__(self):
        self._left = C1(0)
        self._right = C1(0)
        self._left.next = self._right
        self._right.prev = self._left
        self._size = 0

    def _find(self, a1):
        if a1 <= self._size // 2:
            v1 = self._left.next
            for v2 in range(a1):
                v1 = v1.next
            return v1
        v1 = self._right.prev
        for v2 in range(self._size - 1 - a1):
            v1 = v1.prev
        return v1

    def get(self, a1):
        if a1 < 0 or a1 >= self._size:
            return -1
        return self._find(a1).val

    def addAtHead(self, a1):
        v1 = C1(a1)
        v1.next = self._left.next
        v1.prev = self._left
        self._left.next.prev = v1
        self._left.next = v1
        self._size += 1

    def addAtTail(self, a1):
        v1 = C1(a1)
        v1.prev = self._right.prev
        v1.next = self._right
        self._right.prev.next = v1
        self._right.prev = v1
        self._size += 1

    def addAtIndex(self, a1, a2):
        if a1 < 0 or a1 > self._size:
            return
        if a1 == 0:
            self.addAtHead(a2)
            return
        if a1 == self._size:
            self.addAtTail(a2)
            return
        v1 = self._find(a1)
        v2 = C1(a2)
        v2.prev = v1.prev
        v2.next = v1
        v1.prev.next = v2
        v1.prev = v2
        self._size += 1

    def deleteAtIndex(self, a1):
        if a1 < 0 or a1 >= self._size:
            return
        v1 = self._find(a1)
        v1.prev.next = v1.next
        v1.next.prev = v1.prev
        self._size -= 1

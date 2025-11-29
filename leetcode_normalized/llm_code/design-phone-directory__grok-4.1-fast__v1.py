class C1(object):

    def __init__(self, a1):
        self._avail = set(range(a1))
        self._size = a1

    def get(self):
        if self._avail:
            return self._avail.pop()
        return -1

    def check(self, a1):
        return 0 <= a1 < self._size and a1 in self._avail

    def release(self, a1):
        if 0 <= a1 < self._size and a1 not in self._avail:
            self._avail.add(a1)

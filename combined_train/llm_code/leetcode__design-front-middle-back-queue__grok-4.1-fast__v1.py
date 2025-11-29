import collections

class C1:

    def __init__(self):
        self.front = collections.deque()
        self.back = collections.deque()

    def _rebalance(self):
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        if len(self.back) > len(self.front):
            self.front.append(self.back.popleft())

    def pushFront(self, a1):
        self.front.appendleft(a1)
        self._rebalance()

    def pushMiddle(self, a1):
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(a1)

    def pushBack(self, a1):
        self.back.append(a1)
        self._rebalance()

    def popFront(self):
        if self.front:
            v1 = self.front.popleft()
        else:
            return -1
        self._rebalance()
        return v1

    def popMiddle(self):
        if self.front:
            v1 = self.front.pop()
        else:
            return -1
        self._rebalance()
        return v1

    def popBack(self):
        if self.back:
            v1 = self.back.pop()
        elif self.front:
            v1 = self.front.pop()
        else:
            return -1
        self._rebalance()
        return v1

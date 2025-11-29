import collections

class FrontMiddleBackQueue:

    def __init__(self):
        self.front = collections.deque()
        self.back = collections.deque()

    def _rebalance(self):
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        if len(self.back) > len(self.front):
            self.front.append(self.back.popleft())

    def pushFront(self, val):
        self.front.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val):
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)

    def pushBack(self, val):
        self.back.append(val)
        self._rebalance()

    def popFront(self):
        if self.front:
            val = self.front.popleft()
        else:
            return -1
        self._rebalance()
        return val

    def popMiddle(self):
        if self.front:
            val = self.front.pop()
        else:
            return -1
        self._rebalance()
        return val

    def popBack(self):
        if self.back:
            val = self.back.pop()
        elif self.front:
            val = self.front.pop()
        else:
            return -1
        self._rebalance()
        return val

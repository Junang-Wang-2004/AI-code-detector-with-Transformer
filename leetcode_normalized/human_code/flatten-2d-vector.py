from collections import deque

class C1(object):

    def __init__(self, a1):
        """
        Initialize your data structure here.
        """
        self.stack = deque(((len(v), iter(v)) for v1 in a1 if v1))

    def __next__(self):
        """
        """
        v1, v2 = self.stack.popleft()
        if v1 > 1:
            self.stack.appendleft((v1 - 1, v2))
        return next(v2)

    def hasNext(self):
        """
        """
        return bool(self.stack)

import collections

class C1(object):

    def __init__(self, a1, a2):
        """
        Initialize your q structure here.
        """
        self.q = collections.deque([(len(v), iter(v)) for v1 in (a1, a2) if v1])

    def __next__(self):
        """
        """
        len, iter = self.q.popleft()
        if len > 1:
            self.q.append((len - 1, iter))
        return next(iter)

    def hasNext(self):
        """
        """
        return bool(self.q)

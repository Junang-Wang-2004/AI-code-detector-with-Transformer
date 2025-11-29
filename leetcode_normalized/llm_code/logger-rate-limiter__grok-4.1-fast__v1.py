import collections

class C1:

    def __init__(self):
        self.q = collections.deque()
        self.seen = set()

    def cleanup(self, a1):
        while self.q and self.q[0][0] <= a1 - 10:
            v1, v2 = self.q.popleft()
            self.seen.remove(v2)

    def shouldPrintMessage(self, a1, a2):
        self.cleanup(a1)
        if a2 in self.seen:
            return False
        self.q.append((a1, a2))
        self.seen.add(a2)
        return True

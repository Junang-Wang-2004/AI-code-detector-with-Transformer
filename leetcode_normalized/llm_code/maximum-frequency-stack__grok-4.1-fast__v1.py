from collections import Counter, defaultdict, deque

class C1:

    def __init__(self):
        self.frequencies = Counter()
        self.stacks = defaultdict(deque)
        self.highest = 0

    def push(self, a1):
        v1 = self.frequencies[a1]
        v2 = v1 + 1
        self.frequencies[a1] = v2
        self.stacks[v2].append(a1)
        if v2 > self.highest:
            self.highest = v2

    def pop(self):
        v1 = self.stacks[self.highest].pop()
        self.frequencies[v1] -= 1
        if self.frequencies[v1] == 0:
            del self.frequencies[v1]
        if not self.stacks[self.highest]:
            del self.stacks[self.highest]
            self.highest -= 1
        return v1

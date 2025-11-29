import random

class C1:

    def __init__(self):
        self.container = []
        self.mapping = {}

    def insert(self, a1):
        if a1 in self.mapping:
            return False
        self.mapping[a1] = len(self.container)
        self.container.append(a1)
        return True

    def remove(self, a1):
        if a1 not in self.mapping:
            return False
        v1 = self.mapping[a1]
        if v1 != len(self.container) - 1:
            v2 = self.container[-1]
            self.container[v1] = v2
            self.mapping[v2] = v1
        self.container.pop()
        del self.mapping[a1]
        return True

    def getRandom(self):
        return random.choice(self.container)

from collections import defaultdict
from random import randint

class C1:

    def __init__(self):
        self.elements = []
        self.positions = defaultdict(set)

    def insert(self, a1):
        v1 = a1 in self.positions
        self.elements.append(a1)
        self.positions[a1].add(len(self.elements) - 1)
        return not v1

    def remove(self, a1):
        if a1 not in self.positions or not self.positions[a1]:
            return False
        v1 = self.positions[a1].pop()
        v2 = len(self.elements) - 1
        if v1 != v2:
            v3 = self.elements[v2]
            self.positions[v3].discard(v2)
            self.positions[v3].add(v1)
            self.elements[v1] = v3
        self.elements.pop()
        if not self.positions[a1]:
            del self.positions[a1]
        return True

    def getRandom(self):
        v1 = randint(0, len(self.elements) - 1)
        return self.elements[v1]

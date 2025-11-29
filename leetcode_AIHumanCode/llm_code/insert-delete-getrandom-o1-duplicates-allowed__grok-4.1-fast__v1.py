from collections import defaultdict
from random import randint

class RandomizedCollection:

    def __init__(self):
        self.elements = []
        self.positions = defaultdict(set)

    def insert(self, val):
        existed = val in self.positions
        self.elements.append(val)
        self.positions[val].add(len(self.elements) - 1)
        return not existed

    def remove(self, val):
        if val not in self.positions or not self.positions[val]:
            return False
        target_idx = self.positions[val].pop()
        last_idx = len(self.elements) - 1
        if target_idx != last_idx:
            last_val = self.elements[last_idx]
            self.positions[last_val].discard(last_idx)
            self.positions[last_val].add(target_idx)
            self.elements[target_idx] = last_val
        self.elements.pop()
        if not self.positions[val]:
            del self.positions[val]
        return True

    def getRandom(self):
        pick = randint(0, len(self.elements) - 1)
        return self.elements[pick]

import random

class RandomizedSet:

    def __init__(self):
        self.container = []
        self.mapping = {}

    def insert(self, element):
        if element in self.mapping:
            return False
        self.mapping[element] = len(self.container)
        self.container.append(element)
        return True

    def remove(self, element):
        if element not in self.mapping:
            return False
        idx = self.mapping[element]
        if idx != len(self.container) - 1:
            last = self.container[-1]
            self.container[idx] = last
            self.mapping[last] = idx
        self.container.pop()
        del self.mapping[element]
        return True

    def getRandom(self):
        return random.choice(self.container)

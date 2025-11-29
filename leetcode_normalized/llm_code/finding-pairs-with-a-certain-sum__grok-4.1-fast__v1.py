import collections

class C1:

    def __init__(self, a1, a2):
        self.list1 = a1
        self.list2 = a2
        self.freq2 = collections.Counter(a2)

    def add(self, a1, a2):
        v1 = self.list2[a1]
        self.freq2[v1] -= 1
        self.list2[a1] += a2
        self.freq2[self.list2[a1]] += 1

    def count(self, a1):
        return sum((self.freq2[a1 - x] for v1 in self.list1))

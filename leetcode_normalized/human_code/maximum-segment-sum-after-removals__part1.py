class C1(object):

    def __init__(self, a1):
        self.set = list(range(len(a1)))
        self.rank = [0] * len(a1)
        self.size = a1[:]

    def find_set(self, a1):
        v1 = []
        while self.set[a1] != a1:
            v1.append(a1)
            a1 = self.set[a1]
        while v1:
            self.set[v1.pop()] = a1
        return a1

    def union_set(self, a1, a2):
        a1, a2 = (self.find_set(a1), self.find_set(a2))
        if a1 == a2:
            return False
        if self.rank[a1] > self.rank[a2]:
            a1, a2 = (a2, a1)
        self.set[a1] = self.set[a2]
        if self.rank[a1] == self.rank[a2]:
            self.rank[a2] += 1
        self.size[a2] += self.size[a1]
        return True

    def total(self, a1):
        return self.size[self.find_set(a1)]

class C2(object):

    def maximumSegmentSum(self, a1, a2):
        """
        """
        v1 = [0] * len(a2)
        v2 = [0] * len(a1)
        v3 = C1(a1)
        for v4 in reversed(range(1, len(a2))):
            v5 = a2[v4]
            v2[v5] = 1
            if v5 - 1 >= 0 and v2[v5 - 1]:
                v3.union_set(v5 - 1, v5)
            if v5 + 1 < len(a1) and v2[v5 + 1]:
                v3.union_set(v5, v5 + 1)
            v1[v4 - 1] = max(v1[v4], v3.total(v5))
        return v1

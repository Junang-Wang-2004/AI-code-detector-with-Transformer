from functools import reduce

class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1
        self.size = [1] * a1
        self.total = a1

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
        self.total -= 1
        return True

class C2(object):

    def groupStrings(self, a1):
        """
        """
        v1 = C1(len(a1))
        v2 = {}
        for v3, v4 in enumerate(a1):
            v5 = reduce(lambda x, y: v4 | 1 << ord(y) - ord('a'), v4, 0)
            if v5 not in v2:
                v2[v5] = v3
            v1.union_set(v3, v2[v5])
            v6 = 1
            while v6 <= v5:
                if v5 & v6:
                    if v5 ^ v6 not in v2:
                        v2[v5 ^ v6] = v3
                    v1.union_set(v3, v2[v5 ^ v6])
                v6 <<= 1
        return [v1.total, max(v1.size)]

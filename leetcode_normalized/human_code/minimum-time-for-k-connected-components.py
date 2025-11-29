class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1

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
        return True

class C2(object):

    def minTime(self, a1, a2, a3):
        """
        """
        a2.sort(key=lambda x: x[2])
        v1 = 0
        v2 = C1(a1)
        for v3, v4, v5 in reversed(a2):
            if not v2.union_set(v3, v4):
                continue
            if v1 == a1 - a3:
                return v5
            v1 += 1
        return 0

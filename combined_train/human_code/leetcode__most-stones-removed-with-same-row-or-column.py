class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        self.set[min(v1, v2)] = max(v1, v2)
        return True

class C2(object):

    def removeStones(self, a1):
        """
        """
        v1 = 10000
        v2 = C1(2 * v1)
        for v3, v4 in a1:
            v2.union_set(v3, v4 + v1)
        return len(a1) - len({v2.find_set(v3) for v3, v5 in a1})

class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.count = a1

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        self.set[min(v1, v2)] = max(v1, v2)
        self.count -= 1
        return True

class C2(object):

    def minimumCost(self, a1, a2):
        """
        """
        a2.sort(key=lambda x: x[2])
        v1 = C1(a1)
        v2 = 0
        for v3, v4, v5 in a2:
            if v1.union_set(v3 - 1, v4 - 1):
                v2 += v5
        return v2 if v1.count == 1 else -1

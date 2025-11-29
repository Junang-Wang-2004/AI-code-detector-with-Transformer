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
        self.set[max(v1, v2)] = min(v1, v2)
        self.count -= 1
        return True

class C2(object):

    def maxNumEdgesToRemove(self, a1, a2):
        """
        """
        v1 = 0
        v2, v3 = (C1(a1), C1(a1))
        for v4, v5, v6 in a2:
            if v4 != 3:
                continue
            v7 = v2.union_set(v5 - 1, v6 - 1)
            v8 = v3.union_set(v5 - 1, v6 - 1)
            if not v7 and (not v8):
                v1 += 1
        for v4, v5, v6 in a2:
            if v4 == 1:
                if not v2.union_set(v5 - 1, v6 - 1):
                    v1 += 1
            elif v4 == 2:
                if not v3.union_set(v5 - 1, v6 - 1):
                    v1 += 1
        return v1 if v2.count == v3.count == 1 else -1

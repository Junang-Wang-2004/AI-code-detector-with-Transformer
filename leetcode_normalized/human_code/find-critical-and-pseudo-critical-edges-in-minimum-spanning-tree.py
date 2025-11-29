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

    def findCriticalAndPseudoCriticalEdges(self, a1, a2):
        """
        """

        def MST(a1, a2, a3=None, a4=None):
            v1 = C1(a1)
            v2 = 0
            if a4 is not None:
                v3, v4, v5, v6 = a2[a4]
                if v1.union_set(v3, v4):
                    v2 += v5
            for v7, (v3, v4, v5, v6) in enumerate(a2):
                if v7 == a3:
                    continue
                if v1.union_set(v3, v4):
                    v2 += v5
            return v2 if v1.count == 1 else float('inf')
        for v1, v2 in enumerate(a2):
            v2.append(v1)
        a2.sort(key=lambda x: x[2])
        v3 = MST(a1, a2)
        v4 = [[], []]
        for v1, v2 in enumerate(a2):
            if v3 < MST(a1, a2, unused=v1):
                v4[0].append(v2[3])
            elif v3 == MST(a1, a2, used=v1):
                v4[1].append(v2[3])
        return v4

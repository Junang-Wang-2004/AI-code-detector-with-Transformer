import itertools

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

    def areSentencesSimilarTwo(self, a1, a2, a3):
        """
        """
        if len(a1) != len(a2):
            return False
        v1 = {}
        v2 = C1(2 * len(a3))
        for v3 in a3:
            for v4 in v3:
                if v4 not in v1:
                    v1[v4] = len(v1)
            v2.union_set(v1[v3[0]], v1[v3[1]])
        return all((w1 == w2 or (w1 in v1 and w2 in v1 and (v2.find_set(v1[w1]) == v2.find_set(v1[w2]))) for v5, v6 in zip(a1, a2)))

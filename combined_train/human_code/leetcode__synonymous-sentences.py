import collections
import itertools

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
        return True

class C2(object):

    def generateSentences(self, a1, a2):
        """
        """

        def assign_id(a1, a2, a3):
            if a1 in a2:
                return
            a2[a1] = len(a2)
            a3[a2[a1]] = a1
        v1, v2 = ({}, {})
        for v3, v4 in a1:
            (assign_id(v3, v1, v2), assign_id(v4, v1, v2))
        v5 = C1(len(v1))
        for v3, v4 in a1:
            v5.union_set(v1[v3], v1[v4])
        v6 = collections.defaultdict(list)
        for v7 in range(len(v5.set)):
            v6[v5.find_set(v7)].append(v7)
        v8 = []
        for v9 in a2.split(' '):
            if v9 not in v1:
                v8.append([v9])
                continue
            v8.append(sorted([v2[x] for v10 in v6[v5.find_set(v1[v9])]]))
        return [' '.join(sentense) for v11 in itertools.product(*v8)]

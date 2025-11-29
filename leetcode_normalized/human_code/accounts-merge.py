import collections

class C1(object):

    def __init__(self):
        self.set = []

    def get_id(self):
        self.set.append(len(self.set))
        return len(self.set) - 1

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 != v2:
            self.set[min(v1, v2)] = max(v1, v2)

class C2(object):

    def accountsMerge(self, a1):
        """
        """
        v1 = C1()
        v2 = {}
        v3 = {}
        for v4 in a1:
            v5 = v4[0]
            for v6 in range(1, len(v4)):
                if v4[v6] not in v3:
                    v2[v4[v6]] = v5
                    v3[v4[v6]] = v1.get_id()
                v1.union_set(v3[v4[1]], v3[v4[v6]])
        v7 = collections.defaultdict(list)
        for v8 in list(v2.keys()):
            v7[v1.find_set(v3[v8])].append(v8)
        for v9 in list(v7.values()):
            v9.sort()
        return [[v2[v9[0]]] + v9 for v9 in list(v7.values())]

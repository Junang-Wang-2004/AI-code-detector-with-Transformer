import collections
import itertools

class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.__size = a1

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        self.set[min(v1, v2)] = max(v1, v2)
        self.__size -= 1
        return True

    def size(self):
        return self.__size

class C2(object):

    def numSimilarGroups(self, a1):

        def isSimilar(a1, a2):
            v1 = 0
            for v2, v3 in zip(a1, a2):
                if v2 != v3:
                    v1 += 1
                    if v1 > 2:
                        return False
            return v1 == 2
        v1, v2 = (len(a1), len(a1[0]))
        v3 = C1(v1)
        if v1 < v2 * v2:
            for (v4, v5), (v6, v7) in itertools.combinations(enumerate(a1), 2):
                if isSimilar(v5, v7):
                    v3.union_set(v4, v6)
        else:
            v8 = collections.defaultdict(list)
            v9 = set()
            for v10 in range(len(a1)):
                v11 = list(a1[v10])
                if a1[v10] not in v9:
                    v8[a1[v10]].append(v10)
                    v9.add(a1[v10])
                for v12, v13 in itertools.combinations(range(v2), 2):
                    v11[v12], v11[v13] = (v11[v13], v11[v12])
                    v8[''.join(v11)].append(v10)
                    v11[v12], v11[v13] = (v11[v13], v11[v12])
            for v11 in a1:
                for v4, v6 in itertools.combinations(v8[v11], 2):
                    v3.union_set(v4, v6)
        return v3.size()

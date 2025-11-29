import collections

class C1(object):

    def __init__(self, a1):
        self.__root = {}
        self.__bit_count = a1

    def insert(self, a1, a2):
        v1 = self.__root
        for v2 in reversed(range(self.__bit_count)):
            v3 = a1 >> v2 & 1
            v4 = v1.setdefault(v3, collections.defaultdict(int))
            v4['_cnt'] += a2
            if not v4['_cnt']:
                del v1[v3]
                break
            v1 = v4

    def query(self, a1):
        v1, v2 = (self.__root, 0)
        for v3 in reversed(range(self.__bit_count)):
            v4 = a1 >> v3 & 1
            if 1 ^ v4 in v1:
                v1 = v1[1 ^ v4]
                v2 |= 1 << v3
            else:
                v1 = v1[v4]
        return v2

class C2(object):

    def maxGeneticDifference(self, a1, a2):
        """
        """

        def iter_dfs(a1, a2, a3, a4):
            v1 = [(1, a1[-1][0])]
            while v1:
                v2, v3 = v1.pop()
                if v2 == 1:
                    a3.insert(v3, 1)
                    for v4, v5 in a2[v3]:
                        a4[v4] = a3.query(v5)
                    v1.append((2, v3))
                    for v6 in reversed(a1[v3]):
                        v1.append((1, v6))
                elif v2 == 2:
                    a3.insert(v3, -1)
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a1):
            v1[v3].append(v2)
        v4 = collections.defaultdict(list)
        v5 = len(a1) - 1
        for v6, (v2, v7) in enumerate(a2):
            v4[v2].append((v6, v7))
            v5 = max(v5, v7)
        v8 = [0] * len(a2)
        iter_dfs(v1, v4, C1(v5.bit_length()), v8)
        return v8

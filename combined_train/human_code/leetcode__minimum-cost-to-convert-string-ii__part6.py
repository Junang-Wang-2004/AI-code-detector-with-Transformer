import itertools

class C1(object):

    def minimumCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = float('inf')

        class Trie(object):

            def __init__(self):
                self.__nodes = []
                self.__idxs = []
                self.k = 0
                self.__new_node()

            def __new_node(self):
                self.__nodes.append([-1] * 26)
                self.__idxs.append(-1)
                return len(self.__nodes) - 1

            def add(self, a1):
                v1 = 0
                for v2 in a1:
                    v3 = ord(v2) - ord('a')
                    if self.__nodes[v1][v3] == -1:
                        self.__nodes[v1][v3] = self.__new_node()
                    v1 = self.__nodes[v1][v3]
                if self.__idxs[v1] == -1:
                    self.__idxs[v1] = self.k
                    self.k += 1
                    return (True, self.__idxs[v1])
                return (False, self.__idxs[v1])

            def query(self, a1):
                v1 = 0
                for v2 in a1:
                    v1 = self.__nodes[v1][ord(v2) - ord('a')]
                return self.__idxs[v1]

            def next(self, a1, a2):
                return self.__nodes[a1][ord(a2) - ord('a')]

            def id(self, a1):
                return self.__idxs[a1]

        def floydWarshall(a1):
            for v1 in a1.keys():
                for v2 in a1.keys():
                    if a1[v2][v1] == v1:
                        continue
                    for v3 in a1.keys():
                        if a1[v1][v3] == v1:
                            continue
                        a1[v2][v3] = min(a1[v2][v3], a1[v2][v1] + a1[v1][v3])
        v2 = Trie()
        v3 = collections.defaultdict(list)
        for v4 in itertools.chain(a3, a4):
            v5, v6 = v2.add(v4)
            if v5:
                v3[len(v4)].append(v6)
        v7 = {l: {u: {v: 0 if u == v else v1 for v8 in lookup} for v9 in lookup} for v10, v11 in v3.items()}
        for v6 in range(len(a3)):
            v10 = len(a3[v6])
            v12 = v7[v10]
            v9, v8 = (v2.query(a3[v6]), v2.query(a4[v6]))
            v12[v9][v8] = min(v12[v9][v8], a5[v6])
        for v12 in v7.values():
            floydWarshall(v12)
        v13 = [v1] * (max((len(v4) for v4 in a3)) + 1)
        v13[0] = 0
        for v6 in range(len(a1)):
            if v13[v6 % len(v13)] == v1:
                continue
            if a1[v6] == a2[v6]:
                v13[(v6 + 1) % len(v13)] = min(v13[(v6 + 1) % len(v13)], v13[v6 % len(v13)])
            v9 = v8 = 0
            for v14 in range(v6, len(a1)):
                v9 = v2.next(v9, a1[v14])
                v8 = v2.next(v8, a2[v14])
                if v9 == -1 or v8 == -1:
                    break
                if v2.id(v9) != -1 and v2.id(v8) != -1:
                    v13[(v14 + 1) % len(v13)] = min(v13[(v14 + 1) % len(v13)], v13[v6 % len(v13)] + v7[v14 - v6 + 1][v2.id(v9)][v2.id(v8)])
            v13[v6 % len(v13)] = v1
        return v13[len(a1) % len(v13)] if v13[len(a1) % len(v13)] != v1 else -1

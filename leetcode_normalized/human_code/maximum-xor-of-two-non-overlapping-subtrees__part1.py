class C1(object):

    def __init__(self, a1):
        self.__root = {}
        self.__bit_length = a1

    def insert(self, a1):
        v1 = self.__root
        for v2 in reversed(range(self.__bit_length)):
            v3 = a1 >> v2 & 1
            if v3 not in v1:
                v1[v3] = {}
            v1 = v1[v3]

    def query(self, a1):
        if not self.__root:
            return -1
        v1, v2 = (self.__root, 0)
        for v3 in reversed(range(self.__bit_length)):
            v4 = a1 >> v3 & 1
            if 1 ^ v4 in v1:
                v1 = v1[1 ^ v4]
                v2 |= 1 << v3
            else:
                v1 = v1[v4]
        return v2

class C2(object):

    def maxXor(self, a1, a2, a3):
        """
        """

        def iter_dfs():
            v1 = [0] * len(a3)
            v2 = [(1, 0, -1)]
            while v2:
                v3, v4, v5 = v2.pop()
                if v3 == 1:
                    v2.append((2, v4, v5))
                    for v6 in adj[v4]:
                        if v6 == v5:
                            continue
                        v2.append((1, v6, v4))
                elif v3 == 2:
                    v1[v4] = a3[v4] + sum((v1[v6] for v6 in adj[v4] if v6 != v5))
            return v1

        def iter_dfs2():
            v1 = C1(lookup[0].bit_length())
            v2 = [0]
            v3 = [(1, (0, -1, v2))]
            while v3:
                v4, v5 = v3.pop()
                if v4 == 1:
                    v6, v7, v8 = v5
                    v8[0] = max(v1.query(lookup[v6]), 0)
                    v3.append((3, (v6,)))
                    for v9 in adj[v6]:
                        if v9 == v7:
                            continue
                        v10 = [0]
                        v3.append((2, (v10, v8)))
                        v3.append((1, (v9, v6, v10)))
                elif v4 == 2:
                    v10, v8 = v5
                    v8[0] = max(v8[0], v10[0])
                elif v4 == 3:
                    v6 = v5[0]
                    v1.insert(lookup[v6])
            return v2[0]
        v1 = [[] for v2 in range(len(a3))]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = iter_dfs()
        return iter_dfs2()

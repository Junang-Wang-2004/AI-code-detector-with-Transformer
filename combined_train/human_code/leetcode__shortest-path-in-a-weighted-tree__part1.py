class C1(object):

    def __init__(self, a1):
        self.__bit = [0] * (a1 + 1)

    def add(self, a1, a2):
        a1 += 1
        while a1 < len(self.__bit):
            self.__bit[a1] += a2
            a1 += a1 & -a1

    def query(self, a1):
        a1 += 1
        v2 = 0
        while a1 > 0:
            v2 += self.__bit[a1]
            a1 -= a1 & -a1
        return v2

class C2(object):

    def treeQueries(self, a1, a2, a3):
        """
        """

        def iter_dfs():
            v1, v2, v3, v4 = ([0] * a1, [0] * a1, [0] * a1, [0] * a1)
            v5 = 0
            v6 = [(1, (0, -1, 0))]
            while v6:
                v7, v8 = v6.pop()
                if v7 == 1:
                    v9, v10, v11 = v8
                    v1[v9] = v5
                    v5 += 1
                    v3[v9] = v11
                    v6.append((2, (v9,)))
                    for v12, v13 in adj[v9]:
                        if v12 == v10:
                            continue
                        v4[v12] = v13
                        v6.append((1, (v12, v9, v11 + v13)))
                elif v7 == 2:
                    v9 = v8[0]
                    v2[v9] = v5
            return (v1, v2, v3, v4)
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v3 -= 1
            v4 -= 1
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6, v7, v8, v9 = iter_dfs()
        v10 = C1(a1)
        v11 = []
        for v12 in a3:
            if v12[0] == 1:
                v2, v3, v4, v5 = v12
                v3 -= 1
                v4 -= 1
                if v6[v3] > v6[v4]:
                    v3, v4 = (v4, v3)
                v13 = v5 - v9[v4]
                v10.add(v6[v4], v13)
                v10.add(v7[v4], -v13)
                v9[v4] = v5
            else:
                v2, v14 = v12
                v14 -= 1
                v11.append(v8[v14] + v10.query(v6[v14]))
        return v11

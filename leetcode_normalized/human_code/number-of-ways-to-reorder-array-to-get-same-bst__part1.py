v1 = 1000
v2 = 10 ** 9 + 7
v3 = [[0] * v1 for v4 in range(v1)]
for v5 in range(len(v3)):
    v3[v5][0] = 1
    for v6 in range(1, v5 + 1):
        v3[v5][v6] = (v3[v5 - 1][v6 - 1] + v3[v5 - 1][v6]) % v2

class C1(object):

    def numOfWays(self, a1):
        """
        """

        def iter_dfs(a1):
            v1 = [0]
            v2 = [[1, [a1, v1]]]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    a1, v6 = v4
                    if len(a1) <= 2:
                        v6[0] = 1
                        continue
                    v7 = [v for v8 in a1 if v8 < a1[0]]
                    v9 = [v8 for v8 in a1 if v8 > a1[0]]
                    v6[0] = v3[len(v7) + len(v9)][len(v7)]
                    v10, v11 = ([0], [0])
                    v2.append([2, [v10, v11, v6]])
                    v2.append([1, [v9, v11]])
                    v2.append([1, [v7, v10]])
                elif v3 == 2:
                    v10, v11, v6 = v4
                    v6[0] = v6[0] * v10[0] % v2
                    v6[0] = v6[0] * v11[0] % v2
            return v1[0]
        return (iter_dfs(a1) - 1) % v2

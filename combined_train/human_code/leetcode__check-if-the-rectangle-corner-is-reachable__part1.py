class C1(object):

    def canReachCorner(self, a1, a2, a3):
        """
        """

        def check(a1, a2, a3, a4, a5, a6):
            return (a1 - a4) ** 2 + (a2 - a5) ** 2 <= (a3 + a6) ** 2

        def iter_dfs():
            v1 = [False] * len(a3)
            v2 = []
            v3 = [False] * len(a3)
            for v4 in range(len(a3)):
                v5, v6, v7 = a3[v4]
                if v5 - v7 <= 0 or v6 + v7 >= a2:
                    v1[v4] = True
                    v2.append(v4)
                if v5 + v7 >= a1 or v6 - v7 <= 0:
                    v3[v4] = True
            while v2:
                v4 = v2.pop()
                if v3[v4]:
                    return True
                v8, v9, v10 = a3[v4]
                for v11 in range(len(a3)):
                    v12, v13, v14 = a3[v11]
                    if v1[v11] or not check(v8, v9, v10, v12, v13, v14):
                        continue
                    v1[v11] = True
                    v2.append(v11)
            return False
        return not iter_dfs()

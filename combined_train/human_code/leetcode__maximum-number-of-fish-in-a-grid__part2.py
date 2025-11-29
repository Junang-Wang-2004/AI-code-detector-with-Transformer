class C1(object):

    def findMaxFish(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(a1, a2):
            v1 = a1[a1][a2]
            a1[a1][a2] = 0
            v2 = [(a1, a2)]
            while v2:
                a1, a2 = v2.pop()
                for v5, v6 in reversed(v1):
                    v7, v8 = (a1 + v5, a2 + v6)
                    if not (0 <= v7 < len(a1) and 0 <= v8 < len(a1[0]) and a1[v7][v8]):
                        continue
                    v1 += a1[v7][v8]
                    a1[v7][v8] = 0
                    v2.append((v7, v8))
            return v1
        v2 = 0
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                if a1[v3][v4]:
                    v2 = max(v2, dfs(v3, v4))
        return v2

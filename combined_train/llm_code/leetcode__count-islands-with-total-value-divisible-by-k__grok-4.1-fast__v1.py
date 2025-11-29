class C1(object):

    def countIslands(self, a1, a2):
        v1 = len(a1)
        v2 = len(a1[0]) if v1 else 0
        v3 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def flood(a1, a2):
            v1 = a1[a1][a2] % a2
            v2 = [(a1, a2)]
            a1[a1][a2] = 0
            while v2:
                v3, v4 = v2.pop()
                for v5, v6 in v3:
                    v7 = v3 + v5
                    v8 = v4 + v6
                    if 0 <= v7 < v1 and 0 <= v8 < v2 and a1[v7][v8]:
                        v1 = (v1 + a1[v7][v8]) % a2
                        a1[v7][v8] = 0
                        v2.append((v7, v8))
            return v1 == 0
        v4 = 0
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6]:
                    if flood(v5, v6):
                        v4 += 1
        return v4

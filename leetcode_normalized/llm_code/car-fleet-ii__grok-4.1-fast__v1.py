class C1:

    def getCollisionTimes(self, a1):
        v1 = [-1.0] * len(a1)
        v2 = []
        for v3 in range(len(a1) - 1, -1, -1):
            v4, v5 = a1[v3]
            while v2:
                v6, v7, v8 = v2[-1]
                if v7 >= v5:
                    v2.pop()
                    continue
                v9 = (v6 - v4) / (v5 - v7)
                if 0 < v8 <= v9:
                    v2.pop()
                else:
                    break
            if v2:
                v1[v3] = (v2[-1][0] - v4) / (v5 - v2[-1][1])
            v2.append((v4, v5, v1[v3]))
        return v1

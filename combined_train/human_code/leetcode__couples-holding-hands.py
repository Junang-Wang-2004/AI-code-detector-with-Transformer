class C1(object):

    def minSwapsCouples(self, a1):
        """
        """
        v1 = len(a1) // 2
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in enumerate(a1):
            v2[v5 // 2].append(v4 // 2)
        v6 = [[] for v3 in range(v1)]
        for v7, v8 in v2:
            v6[v7].append(v8)
            v6[v8].append(v7)
        v9 = 0
        for v10 in range(v1):
            if not v6[v10]:
                continue
            v7, v8 = (v10, v6[v10].pop())
            while v8 != v10:
                v9 += 1
                v6[v8].remove(v7)
                v7, v8 = (v8, v6[v8].pop())
        return v9

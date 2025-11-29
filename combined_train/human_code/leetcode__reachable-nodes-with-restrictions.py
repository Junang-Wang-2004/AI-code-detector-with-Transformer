class C1(object):

    def reachableNodes(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = 0
        v6 = [False] * a1
        for v7 in a3:
            v6[v7] = True
        v8 = [0]
        v6[0] = True
        while v8:
            v9 = []
            for v3 in v8:
                v5 += 1
                for v4 in v1[v3]:
                    if v6[v4]:
                        continue
                    v6[v4] = True
                    v9.append(v4)
            v8 = v9
        return v5

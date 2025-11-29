class C1(object):

    def getAncestors(self, a1, a2):
        """
        """
        v1 = [set() for v2 in range(a1)]
        v3 = [0] * a1
        v4 = [[] for v2 in range(a1)]
        for v5, v6 in a2:
            v4[v5].append(v6)
            v3[v6] += 1
            v1[v6].add(v5)
        v7 = [v5 for v5, v8 in enumerate(v3) if not v8]
        while v7:
            v9 = []
            for v5 in v7:
                for v6 in v4[v5]:
                    v1[v6].update(v1[v5])
                    v3[v6] -= 1
                    if not v3[v6]:
                        v9.append(v6)
            v7 = v9
        return [sorted(s) for v10 in v1]

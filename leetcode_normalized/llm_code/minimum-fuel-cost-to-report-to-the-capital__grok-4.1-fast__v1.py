class C1(object):

    def minimumFuelCost(self, a1, a2):
        v1 = len(a1) + 1
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [0]

        def traverse(a1, a2):
            v1 = 1
            for v2 in v2[a1]:
                if v2 != a2:
                    v3 = traverse(v2, a1)
                    v6[0] += (v3 + a2 - 1) // a2
                    v1 += v3
            return v1
        traverse(0, -1)
        return v6[0]

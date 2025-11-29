class C1(object):

    def minimumHammingDistance(self, a1, a2, a3):
        """
        """

        def iter_flood_fill(a1, a2, a3, a4):
            v1 = [a2]
            while v1:
                a2 = v1.pop()
                if a2 in a3:
                    continue
                a3.add(a2)
                a4.append(a2)
                for v3 in a1[a2]:
                    v1.append(v3)
        v1 = [set() for v2 in range(len(a1))]
        for v2, v3 in a3:
            v1[v2].add(v3)
            v1[v3].add(v2)
        v4 = 0
        v5 = set()
        for v2 in range(len(a1)):
            if v2 in v5:
                continue
            v6 = []
            iter_flood_fill(v1, v2, v5, v6)
            v7 = collections.Counter([a1[v2] for v2 in v6])
            v8 = collections.Counter([a2[v2] for v2 in v6])
            v9 = v7 - v8
            v4 += sum(v9.values())
        return v4

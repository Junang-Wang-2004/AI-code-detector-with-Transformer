class C1(object):

    def isPrintable(self, a1):
        """
        """
        v1, v2 = list(range(2))

        def has_cycle(a1, a2, a3):
            a3[a2] = v1
            for v1 in a1[a2]:
                if v1 not in a3 and has_cycle(a1, v1, a3) or a3[v1] == v1:
                    return True
            a3[a2] = v2
            return False
        v3 = 60
        v4 = collections.defaultdict(set)
        for v5 in range(1, v3 + 1):
            v6 = len(a1)
            v7 = len(a1[0])
            v8 = -1
            v9 = -1
            for v10 in range(len(a1)):
                for v11 in range(len(a1[v10])):
                    if a1[v10][v11] == v5:
                        v6 = min(v6, v10)
                        v7 = min(v7, v11)
                        v8 = max(v8, v10)
                        v9 = max(v9, v11)
            for v10 in range(v6, v8 + 1):
                for v11 in range(v7, v9 + 1):
                    if a1[v10][v11] != v5:
                        v4[v5].add(a1[v10][v11])
        v12 = {}
        return all((v5 in v12 or not has_cycle(v4, v5, v12) for v5 in range(1, v3 + 1)))

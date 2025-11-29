class C1(object):

    def palindromePairs(self, a1):
        """
        """

        def manacher(a1, a2):

            def preProcess(a1):
                if not a1:
                    return ['^', '$']
                v1 = ['^']
                for v2 in a1:
                    v1 += ['#', v2]
                v1 += ['#', '$']
                return v1
            v1 = preProcess(a1)
            v2, v3 = (0, 0)
            for v4 in range(1, len(v1) - 1):
                v5 = 2 * v2 - v4
                if v3 > v4:
                    a2[v4] = min(v3 - v4, a2[v5])
                else:
                    a2[v4] = 0
                while v1[v4 + 1 + a2[v4]] == v1[v4 - 1 - a2[v4]]:
                    a2[v4] += 1
                if v4 + a2[v4] > v3:
                    v2, v3 = (v4, v4 + a2[v4])
        v1, v2 = (collections.defaultdict(list), collections.defaultdict(list))
        for v3, v4 in enumerate(a1):
            v5 = [0] * (2 * len(v4) + 3)
            manacher(v4, v5)
            for v6 in range(len(v5)):
                if v6 - v5[v6] == 1:
                    v1[v4[(v6 + v5[v6]) // 2:]].append(v3)
                if v6 + v5[v6] == len(v5) - 2:
                    v2[v4[:(v6 - v5[v6]) // 2]].append(v3)
        v7 = []
        for v3, v4 in enumerate(a1):
            for v6 in v1[v4[::-1]]:
                if v6 != v3:
                    v7.append([v3, v6])
            for v6 in v2[v4[::-1]]:
                if len(v4) != len(a1[v6]):
                    v7.append([v6, v3])
        return v7

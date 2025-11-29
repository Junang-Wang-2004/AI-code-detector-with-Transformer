class C1(object):

    def secondMinimum(self, a1, a2, a3, a4):
        """
        """

        def bi_bfs(a1, a2, a3):
            v1, v2 = ({a2}, {a3})
            v3 = set()
            v4 = v5 = 0
            while v1 and (not v4 or v4 + 2 > v5):
                for v6 in v1:
                    v3.add(v6)
                v7 = set()
                for v6 in v1:
                    if v6 in v2:
                        if not v4:
                            v4 = v5
                        elif v4 < v5:
                            return v4 + 1
                    for v8 in a1[v6]:
                        if v8 in v3:
                            continue
                        v7.add(v8)
                v1 = v7
                v5 += 1
                if len(v1) > len(v2):
                    v1, v2 = (v2, v1)
            return v4 + 2

        def calc_time(a1, a2, a3):
            v1 = 0
            for v2 in range(a3):
                if v1 // a2 % 2:
                    v1 = (v1 // a2 + 1) * a2
                v1 += a1
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3 - 1].append(v4 - 1)
            v1[v4 - 1].append(v3 - 1)
        return calc_time(a3, a4, bi_bfs(v1, 0, a1 - 1))

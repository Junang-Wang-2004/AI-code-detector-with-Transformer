class C1(object):

    def minSplitMerge(self, a1, a2):
        """
        """

        def bfs(a1, a2):

            def adj(a1):
                for v1 in range(len(a1)):
                    for v2 in range(v1, len(a1)):
                        v3 = a1[v1:v2 + 1]
                        v4 = a1[:v1] + a1[v2 + 1:]
                        for v5 in range(len(v4) + 1):
                            if v5 == v1:
                                continue
                            yield (v4[:v5] + v3 + v4[v5:])
            v1 = 0
            if a1 == a2:
                return v1
            v2 = {a1}
            v3 = [a1]
            v1 += 1
            while v3:
                v4 = []
                for v5 in v3:
                    for v6 in adj(v5):
                        if v6 in v2:
                            continue
                        if v6 == a2:
                            return v1
                        v2.add(v6)
                        v4.append(v6)
                v3 = v4
                v1 += 1
            return -1
        return bfs(tuple(a1), tuple(a2))

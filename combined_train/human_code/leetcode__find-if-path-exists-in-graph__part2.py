class C1(object):

    def validPath(self, a1, a2, a3, a4):
        """
        """

        def bfs(a1, a2, a3):
            v1 = [a2]
            v2 = set(v1)
            v3 = 0
            while v1:
                v4 = []
                for v5 in v1:
                    if v5 == a3:
                        return v3
                    for v6 in a1[v5]:
                        if v6 in v2:
                            continue
                        v2.add(v6)
                        v4.append(v6)
                v1 = v4
                v3 += 1
            return -1
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        return bfs(v1, a3, a4) >= 0

class C1(object):

    def maximumInvitations(self, a1):
        """
        """

        def find_cycles(a1):
            v1 = []
            v2 = [False] * len(a1)
            for v3 in range(len(a1)):
                v4 = {}
                while not v2[v3]:
                    v2[v3] = True
                    v4[v3] = len(v4)
                    v3 = a1[v3]
                if v3 in v4:
                    v1.append((v3, len(v4) - v4[v3]))
            return v1

        def bfs(a1, a2, a3):
            v1 = 0
            v2 = [a2]
            while v2:
                v1 += 1
                v3 = []
                for a2 in v2:
                    for v5 in a1[a2]:
                        if v5 == a3:
                            continue
                        v3.append(v5)
                v2 = v3
            return v1
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in enumerate(a1):
            v1[v4].append(v3)
        v5 = find_cycles(a1)
        return max(max([l for v2, v6 in v5 if v6 > 2] or [0]), sum((bfs(v1, v3, a1[v3]) + bfs(v1, a1[v3], v3) for v3, v6 in v5 if v6 == 2)))

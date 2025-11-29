class C1(object):

    def cutOffTree(self, a1):
        """
        """

        def minStep(a1, a2):
            v1 = 0
            v2 = {a1}
            v3 = collections.deque([a1])
            while v3:
                v4 = len(v3)
                for v5 in range(v4):
                    v6, v7 = v3.popleft()
                    if (v6, v7) == a2:
                        return v1
                    for v6, v7 in ((v6 + 1, v7), (v6 - 1, v7), (v6, v7 + 1), (v6, v7 - 1)):
                        if not (0 <= v6 < m and 0 <= v7 < n and a1[v6][v7] and ((v6, v7) not in v2)):
                            continue
                        v3.append((v6, v7))
                        v2.add((v6, v7))
                v1 += 1
            return -1
        v1, v2 = (len(a1), len(a1[0]))
        v3 = []
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5] > 1:
                    heapq.heappush(v3, (a1[v4][v5], (v4, v5)))
        v6 = (0, 0)
        v7 = 0
        while v3:
            v8 = heapq.heappop(v3)
            v9 = minStep(v6, v8[1])
            if v9 < 0:
                return -1
            v7 += v9
            v6 = v8[1]
        return v7

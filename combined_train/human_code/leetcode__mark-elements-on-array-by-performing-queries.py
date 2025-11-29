class C1(object):

    def unmarkedSumArray(self, a1, a2):
        """
        """
        v1 = sum(a1)
        v2 = [False] * len(a1)
        v3 = [(x, i) for v4, v5 in enumerate(a1)]
        heapq.heapify(v3)
        v6 = []
        for v4, v7 in a2:
            if not v2[v4]:
                v2[v4] = True
                v1 -= a1[v4]
            for v8 in range(v7):
                while v3:
                    v5, v4 = heapq.heappop(v3)
                    if v2[v4]:
                        continue
                    v2[v4] = True
                    v1 -= v5
                    break
                if not v3:
                    break
            v6.append(v1)
        return v6

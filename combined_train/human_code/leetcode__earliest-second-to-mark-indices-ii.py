import heapq

class C1(object):

    def earliestSecondToMarkIndices(self, a1, a2):
        """
        """

        def check(a1):
            v1 = []
            v2 = 0
            for v3 in reversed(range(a1)):
                if v3 != lookup[a2[v3] - 1]:
                    v2 += 1
                    continue
                heapq.heappush(v1, a1[a2[v3] - 1])
                if v2:
                    v2 -= 1
                else:
                    v2 += 1
                    heapq.heappop(v1)
            return total - (sum(v1) + len(v1)) <= v2
        v1 = [-1] * len(a1)
        for v2 in reversed(range(len(a2))):
            if a1[a2[v2] - 1]:
                v1[a2[v2] - 1] = v2
        v3 = sum(a1) + len(a1)
        v4, v5 = (sum((1 if v1[v2] != -1 else a1[v2] for v2 in range(len(a1)))) + len(a1), len(a2))
        while v4 <= v5:
            v6 = v4 + (v5 - v4) // 2
            if check(v6):
                v5 = v6 - 1
            else:
                v4 = v6 + 1
        return v4 if v4 <= len(a2) else -1

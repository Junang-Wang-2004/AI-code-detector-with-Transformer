import heapq

class C1(object):

    def getFinalState(self, a1, a2, a3):
        """
        """
        if a3 == 1:
            return a1
        v1 = [(x, i) for v2, v3 in enumerate(a1)]
        heapq.heapify(v1)
        v4 = max(a1)
        for a2 in reversed(range(1, a2 + 1)):
            if v1[0][0] * a3 > v4:
                break
            v3, v2 = heapq.heappop(v1)
            heapq.heappush(v1, (v3 * a3, v2))
        else:
            a2 = 0
        v6 = sorted(v1)
        v7, v8 = divmod(a2, len(a1))
        v9 = pow(a3, v7)
        v10 = [0] * len(a1)
        for v11, (v3, v2) in enumerate(v6):
            v10[v2] = v3 * v9 * (a3 if v11 < v8 else 1)
        return v10

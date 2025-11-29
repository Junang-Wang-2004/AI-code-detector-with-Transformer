import heapq

class C1(object):

    def getFinalState(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        if a3 == 1:
            return a1
        v2 = [(x, i) for v3, v4 in enumerate(a1)]
        heapq.heapify(v2)
        v5 = max(a1)
        for a2 in reversed(range(1, a2 + 1)):
            if v2[0][0] * a3 > v5:
                break
            v4, v3 = heapq.heappop(v2)
            heapq.heappush(v2, (v4 * a3, v3))
        else:
            a2 = 0
        v7 = sorted(v2)
        v8, v9 = divmod(a2, len(a1))
        v10 = pow(a3, v8, v1)
        v11 = [0] * len(a1)
        for v12, (v4, v3) in enumerate(v7):
            v11[v3] = v4 * v10 * (a3 if v12 < v9 else 1) % v1
        return v11

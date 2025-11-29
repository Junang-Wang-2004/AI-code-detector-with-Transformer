import heapq
import collections

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """

        def get_top(a1, a2, a3):
            while a1[0] in a2:
                v1 = heapq.heappop(a1)
                a2[v1] -= 1
                if a2[v1] == 0:
                    del a2[v1]
                a3[0] -= 1
            return a1[0]

        def lazy_delete(a1, a2, a3, a4):
            a2[a4] += 1
            a3[0] += 1
            if a3[0] <= len(a1) - a3[0]:
                return
            v1 = []
            for a4 in a1:
                if a4 not in a2:
                    v1.append(a4)
                    continue
                a2[a4] -= 1
                if a2[a4] == 0:
                    del a2[a4]
            a3[0] = 0
            heapq.heapify(v1)
            a1[:] = v1
        v1, v2 = ([], [])
        v3, v4 = (collections.Counter(), collections.Counter())
        v5, v6 = ([0], [0])
        v7, v8 = (float('inf'), 0)
        for v9 in range(1, len(a1)):
            heapq.heappush(v1, -a1[v9])
            v8 += a1[v9]
            if len(v1) - v5[0] > a2 - 1:
                v10 = get_top(v1, v3, v5)
                v8 -= -v10
                heapq.heappush(v2, -heapq.heappop(v1))
            if len(v1) - v5[0] + (len(v2) - v6[0]) > 1 + a3:
                v10 = get_top(v2, v4, v6)
                if v10 <= a1[v9 - (1 + a3)]:
                    lazy_delete(v2, v4, v6, a1[v9 - (1 + a3)])
                else:
                    lazy_delete(v1, v3, v5, -a1[v9 - (1 + a3)])
                    heapq.heappop(v2)
                    v8 -= a1[v9 - (1 + a3)] - v10
                    heapq.heappush(v1, -v10)
            if len(v1) - v5[0] == a2 - 1:
                v7 = min(v7, v8)
        return a1[0] + v7

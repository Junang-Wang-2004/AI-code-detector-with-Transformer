import heapq

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """

        def get_top(a1, a2):
            while abs(a1[0][1]) < i - (1 + a3):
                heapq.heappop(a1)
                a2[0] -= 1
            return a1[0]

        def lazy_delete(a1, a2):
            a2[0] += 1
            if a2[0] <= len(a1) - a2[0]:
                return
            a1[:] = [x for v1 in a1 if abs(v1[1]) > i - (1 + a3)]
            heapq.heapify(a1)
            a2[0] = 0
        v1, v2 = ([], [])
        v3, v4 = ([0], [0])
        v5, v6 = (float('inf'), 0)
        for v7 in range(1, len(a1)):
            heapq.heappush(v1, (-a1[v7], v7))
            v6 += a1[v7]
            if v7 > a2 - 1:
                v8, v9 = get_top(v1, v3)
                heapq.heappop(v1)
                v6 -= -v8
                heapq.heappush(v2, (-v8, -v9))
            if v7 > 1 + a3:
                v8, v9 = get_top(v2, v4)
                if (v8, v9) <= (a1[v7 - (1 + a3)], -(v7 - (1 + a3))):
                    lazy_delete(v2, v4)
                else:
                    lazy_delete(v1, v3)
                    heapq.heappop(v2)
                    v6 -= a1[v7 - (1 + a3)] - v8
                    heapq.heappush(v1, (-v8, -v9))
            if v7 >= a2 - 1:
                v5 = min(v5, v6)
        return a1[0] + v5

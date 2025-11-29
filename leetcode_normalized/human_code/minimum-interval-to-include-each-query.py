import heapq

class C1(object):

    def minInterval(self, a1, a2):
        """
        """
        a1.sort()
        a2 = [(q, i) for v2, v3 in enumerate(a2)]
        a2.sort()
        v4 = []
        v2 = 0
        v5 = [-1] * len(a2)
        for v3, v6 in a2:
            while v2 != len(a1) and a1[v2][0] <= v3:
                heapq.heappush(v4, [a1[v2][1] - a1[v2][0] + 1, v2])
                v2 += 1
            while v4 and a1[v4[0][1]][1] < v3:
                heapq.heappop(v4)
            v5[v6] = v4[0][0] if v4 else -1
        return v5

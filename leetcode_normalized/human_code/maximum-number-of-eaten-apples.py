import heapq

class C1(object):

    def eatenApples(self, a1, a2):
        """
        """
        v1 = []
        v2 = v3 = 0
        while v3 < len(a1) or v1:
            if v3 < len(a1) and a1[v3] > 0:
                heapq.heappush(v1, [v3 + a2[v3], v3])
            while v1 and (v1[0][0] <= v3 or a1[v1[0][1]] == 0):
                heapq.heappop(v1)
            if v1:
                a1[v1[0][1]] -= 1
                v2 += 1
            v3 += 1
        return v2

import heapq

class C1(object):

    def getOrder(self, a1):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a1[x][0])
        v2, v3 = ([], [])
        v4, v5 = (0, a1[v1[0]][0])
        while v4 < len(v1) or v3:
            while v4 < len(v1) and a1[v1[v4]][0] <= v5:
                heapq.heappush(v3, (a1[v1[v4]][1], v1[v4]))
                v4 += 1
            if not v3:
                v5 = a1[v1[v4]][0]
                continue
            v6, v7 = heapq.heappop(v3)
            v5 += v6
            v2.append(v7)
        return v2

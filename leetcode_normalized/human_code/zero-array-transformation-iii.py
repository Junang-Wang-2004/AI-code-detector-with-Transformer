import heapq

class C1(object):

    def maxRemoval(self, a1, a2):
        """
        """
        a2.sort(reverse=True)
        v1, v2 = ([], [])
        for v3 in range(len(a1)):
            while a2 and a2[-1][0] <= v3:
                heapq.heappush(v1, -a2.pop()[1])
            while v2 and v2[0] < v3:
                heapq.heappop(v2)
            while len(v2) < a1[v3]:
                if not v1 or -v1[0] < v3:
                    return -1
                heapq.heappush(v2, -heapq.heappop(v1))
        return len(v1)

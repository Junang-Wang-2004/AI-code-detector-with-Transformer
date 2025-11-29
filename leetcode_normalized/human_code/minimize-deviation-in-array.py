import heapq

class C1(object):

    def minimumDeviation(self, a1):
        """
        """
        v1 = [-num * 2 if num % 2 else -num for v2 in a1]
        heapq.heapify(v1)
        v3 = -max(v1)
        v4 = float('inf')
        while len(v1) == len(a1):
            v2 = -heapq.heappop(v1)
            v4 = min(v4, v2 - v3)
            if not v2 % 2:
                v3 = min(v3, v2 // 2)
                heapq.heappush(v1, -v2 // 2)
        return v4

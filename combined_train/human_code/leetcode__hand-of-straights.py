from collections import Counter
from heapq import heapify, heappop

class C1(object):

    def isNStraightHand(self, a1, a2):
        """
        """
        if len(a1) % a2:
            return False
        v1 = Counter(a1)
        v2 = list(a1)
        heapify(v2)
        for v3 in range(len(v2) // a2):
            while v1[v2[0]] == 0:
                heappop(v2)
            v4 = heappop(v2)
            for v3 in range(a2):
                v1[v4] -= 1
                if v1[v4] < 0:
                    return False
                v4 += 1
        return True

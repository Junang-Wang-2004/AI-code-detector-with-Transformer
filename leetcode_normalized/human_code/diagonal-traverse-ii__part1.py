import itertools
import collections

class C1(object):

    def findDiagonalOrder(self, a1):
        """
        """
        v1, v2, v3 = ([], collections.deque(), 0)
        for v4 in range(len(a1) + max(map(len, a1)) - 1):
            v5 = collections.deque()
            if v4 < len(a1):
                v2.appendleft((v4, 0))
            for v6, v7 in v2:
                v1.append(a1[v6][v7])
                if v7 + 1 < len(a1[v6]):
                    v5.append((v6, v7 + 1))
            v2 = v5
        return v1

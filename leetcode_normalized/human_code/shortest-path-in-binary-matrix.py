import collections

class C1(object):

    def shortestPathBinaryMatrix(self, a1):
        """
        """
        v1 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        v2 = 0
        v3 = collections.deque([(0, 0)])
        while v3:
            v2 += 1
            v4 = collections.deque()
            while v3:
                v5, v6 = v3.popleft()
                if 0 <= v5 < len(a1) and 0 <= v6 < len(a1[0]) and (not a1[v5][v6]):
                    a1[v5][v6] = 1
                    if v5 == len(a1) - 1 and v6 == len(a1) - 1:
                        return v2
                    for v7 in v1:
                        v4.append((v5 + v7[0], v6 + v7[1]))
            v3 = v4
        return -1

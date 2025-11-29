import collections

class C1(object):

    def minimumEffortPath(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def check(a1, a2):
            v1 = [[False] * len(a1[0]) for v2 in range(len(a1))]
            v3 = collections.deque([(0, 0)])
            while v3:
                v4, v5 = v3.popleft()
                if (v4, v5) == (len(a1) - 1, len(a1[0]) - 1):
                    return True
                for v6, v7 in v1:
                    v8, v9 = (v4 + v6, v5 + v7)
                    if not (0 <= v8 < len(a1) and 0 <= v9 < len(a1[0]) and (abs(a1[v8][v9] - a1[v4][v5]) <= a2) and (not v1[v8][v9])):
                        continue
                    v1[v8][v9] = True
                    v3.append((v8, v9))
            return False
        v2, v3 = (0, 10 ** 6)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if check(a1, v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v2

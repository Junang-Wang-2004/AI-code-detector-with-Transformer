import collections

class C1(object):

    def minCost(self, a1):
        """
        """
        v1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        v2, v3 = ((0, 0), (len(a1) - 1, len(a1[0]) - 1))
        v4 = collections.deque([(v2, 0)])
        v5 = set()
        while v4:
            v2, v6 = v4.popleft()
            if v2 in v5:
                continue
            v5.add(v2)
            if v2 == v3:
                return v6
            for v7, (v8, v9) in enumerate(v1, 1):
                v10 = (v2[0] + v8, v2[1] + v9)
                if not (0 <= v10[0] < len(a1) and 0 <= v10[1] < len(a1[0]) and (v10 not in v5)):
                    continue
                if v7 == a1[v2[0]][v2[1]]:
                    v4.appendleft((v10, v6))
                else:
                    v4.append((v10, v6 + 1))
        return -1

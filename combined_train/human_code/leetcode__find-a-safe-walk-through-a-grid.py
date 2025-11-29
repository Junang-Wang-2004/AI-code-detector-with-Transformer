import collections

class C1(object):

    def findSafeWalk(self, a1, a2):
        """
        """
        v1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        v2, v3 = ((0, 0), (len(a1) - 1, len(a1[0]) - 1))
        if not 0 + a1[0][0] < a2:
            return False
        v4 = collections.deque([(v2, a1[0][0])])
        v5 = set()
        while v4:
            v2, v6 = v4.popleft()
            if v2 in v5:
                continue
            v5.add(v2)
            if v2 == v3:
                return True
            for v7, v8 in v1:
                v9 = (v2[0] + v7, v2[1] + v8)
                if not (0 <= v9[0] < len(a1) and 0 <= v9[1] < len(a1[0]) and (v9 not in v5)):
                    continue
                if not a1[v9[0]][v9[1]]:
                    v4.appendleft((v9, v6))
                elif v6 + 1 < a2:
                    v4.append((v9, v6 + 1))
        return False

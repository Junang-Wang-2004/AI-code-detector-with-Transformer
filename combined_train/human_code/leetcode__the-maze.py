import collections

class C1(object):

    def hasPath(self, a1, a2, a3):
        """
        """

        def neighbors(a1, a2):
            for v1, v2 in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                v3, v4 = a2
                while 0 <= v3 + v1 < len(a1) and 0 <= v4 + v2 < len(a1[0]) and (not a1[v3 + v1][v4 + v2]):
                    v3 += v1
                    v4 += v2
                yield (v3, v4)
        a2, a3 = (tuple(a2), tuple(a3))
        v3 = collections.deque([a2])
        v4 = set()
        while v3:
            v5 = v3.popleft()
            if v5 in v4:
                continue
            if v5 == a3:
                return True
            v4.add(v5)
            for v6 in neighbors(a1, v5):
                v3.append(v6)
        return False

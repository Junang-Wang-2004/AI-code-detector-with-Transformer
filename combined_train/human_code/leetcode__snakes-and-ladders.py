import collections

class C1(object):

    def snakesAndLadders(self, a1):
        """
        """

        def coordinate(a1, a2):
            v1, v2 = divmod(a2 - 1, a1)
            v3 = a1 - 1 - v1
            v4 = v2 if v3 % 2 != a1 % 2 else a1 - 1 - v2
            return (v3, v4)
        v1 = len(a1)
        v2 = {1: 0}
        v3 = collections.deque([1])
        while v3:
            v4 = v3.popleft()
            if v4 == v1 * v1:
                return v2[v4]
            for v5 in range(v4 + 1, min(v4 + 6, v1 * v1) + 1):
                v6, v7 = coordinate(v1, v5)
                if a1[v6][v7] != -1:
                    v5 = a1[v6][v7]
                if v5 not in v2:
                    v2[v5] = v2[v4] + 1
                    v3.append(v5)
        return -1

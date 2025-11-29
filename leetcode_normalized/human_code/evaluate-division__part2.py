import collections
import itertools

class C1(object):

    def calcEquation(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(dict)
        for (v2, v3), v4 in zip(a1, a2):
            v1[v2][v3] = v4
            v1[v3][v2] = 1.0 / v4

        def bfs(a1, a2, a3, a4):
            if a2 not in a1 or a3 not in a1:
                return -1.0
            if (a2, a3) in a4:
                return a4[a2, a3]
            v1 = {a2}
            v2 = collections.deque([(a2, 1.0)])
            while v2:
                v3, v4 = v2.popleft()
                if v3 == a3:
                    a4[a2, a3] = v4
                    return v4
                for v5, v6 in a1[v3].items():
                    if v5 in v1:
                        continue
                    v1.add(v5)
                    v2.append((v5, v4 * v6))
            a4[a2, a3] = -1.0
            return -1.0
        v5 = {}
        return [bfs(v1, v2, v3, v5) for v2, v3 in a3]

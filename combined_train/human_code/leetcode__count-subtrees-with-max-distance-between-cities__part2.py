import collections
import math

class C1(object):

    def countSubgraphsForEachDiameter(self, a1, a2):
        """
        """

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1

        def bfs(a1, a2, a3):
            v1 = collections.deque([(a3, 0)])
            v2 = 1 << a3
            v3 = popcount(a2) - 1
            v4, v5 = (None, None)
            while v1:
                v4, v5 = v1.popleft()
                for v6 in a1[v4]:
                    if not a2 & 1 << v6 or v2 & 1 << v6:
                        continue
                    v2 |= 1 << v6
                    v3 -= 1
                    v1.append((v6, v5 + 1))
            return (v3 == 0, v4, v5)

        def max_distance(a1, a2, a3, a4):
            v1, v2, v3 = bfs(a3, a4, int(math.log(a4 & -a4, 2)))
            return bfs(a3, a4, v2)[-1] if v1 else 0
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v2 -= 1
            v3 -= 1
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = [0] * (a1 - 1)
        for v5 in range(1, 2 ** a1):
            v6 = max_distance(a1, a2, v1, v5)
            if v6 - 1 >= 0:
                v4[v6 - 1] += 1
        return v4

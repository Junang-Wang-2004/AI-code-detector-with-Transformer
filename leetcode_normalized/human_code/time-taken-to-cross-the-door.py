import collections
import itertools

class C1(object):

    def timeTaken(self, a1, a2):
        """
        """

        def go_until(a1):
            while curr[0] <= a1 and any(q):
                if not q[direction[0]]:
                    direction[0] ^= 1
                result[q[direction[0]].popleft()] = curr[0]
                curr[0] += 1
        v1, v2, v3 = list(range(-1, 1 + 1))
        v4 = [0] * len(a1)
        v5, v6 = ([float('-inf')], [v1])
        v7 = [collections.deque(), collections.deque()]
        for v8, (v9, v10) in enumerate(zip(a1, a2)):
            go_until(v9 - 1)
            v7[v10].append(v8)
            if not v9 <= v5[0]:
                v5, v6 = ([v9], [v3])
        go_until(float('inf'))
        return v4

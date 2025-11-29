import collections
import itertools

class C1(object):

    def maxJumps(self, a1, a2):
        """
        """

        def dp(a1, a2, a3, a4, a5, a6):
            if a6[a3]:
                return a6[a3]
            a6[a3] = 1
            for v1 in itertools.chain(a4[a3], a5[a3]):
                a6[a3] = max(a6[a3], dp(a1, a2, v1, a4, a5, a6) + 1)
            return a6[a3]
        v1, v2 = ([[] for v3 in range(len(a1))], collections.deque())
        for v4 in range(len(a1)):
            if v2 and v4 - v2[0] == a2 + 1:
                v2.popleft()
            while v2 and a1[v2[-1]] < a1[v4]:
                if v1[v4] and a1[v1[v4][-1]] != a1[v2[-1]]:
                    v1[v4] = []
                v1[v4].append(v2.pop())
            v2.append(v4)
        v5, v2 = ([[] for v3 in range(len(a1))], collections.deque())
        for v4 in reversed(range(len(a1))):
            if v2 and v2[0] - v4 == a2 + 1:
                v2.popleft()
            while v2 and a1[v2[-1]] < a1[v4]:
                if v5[v4] and a1[v5[v4][-1]] != a1[v2[-1]]:
                    v5[v4] = []
                v5[v4].append(v2.pop())
            v2.append(v4)
        v6 = [0] * len(a1)
        return max(map(lambda x: dp(a1, a2, x, v1, v5, v6), range(len(a1))))

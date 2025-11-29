import collections

class C1(object):

    def countNonDecreasingSubarrays(self, a1, a2):
        """
        """
        v1 = v2 = 0
        v3 = collections.deque()
        v4 = len(a1) - 1
        for v5 in reversed(range(len(a1))):
            while v3 and a1[v3[-1]] < a1[v5]:
                v6 = v3.pop()
                v7 = v3[-1] - 1 if v3 else v4
                v2 += (v7 - v6 + 1) * (a1[v5] - a1[v6])
            v3.append(v5)
            while v2 > a2:
                v2 -= a1[v3[0]] - a1[v4]
                if v3[0] == v4:
                    v3.popleft()
                v4 -= 1
            v1 += v4 - v5 + 1
        return v1

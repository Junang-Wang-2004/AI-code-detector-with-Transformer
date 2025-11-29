import collections

class C1(object):

    def longestBalanced(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v3 = collections.defaultdict(int)
            v4 = 0
            for v5 in range(v2, len(a1)):
                v3[a1[v5]] += 1
                v4 = max(v4, v3[a1[v5]])
                if (v5 - v2 + 1) % len(v3) == 0 and (v5 - v2 + 1) // len(v3) == v4:
                    v1 = max(v1, v5 - v2 + 1)
        return v1

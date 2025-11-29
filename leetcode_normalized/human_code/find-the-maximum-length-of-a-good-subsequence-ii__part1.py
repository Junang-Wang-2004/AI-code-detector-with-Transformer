import collections

class C1(object):

    def maximumLength(self, a1, a2):
        """
        """
        v1 = {x: i for v2, v3 in enumerate(set(a1))}
        v4 = [[0] * len(v1) for v5 in range(a2 + 1)]
        v6 = [0] * (a2 + 1)
        for v3 in a1:
            v3 = v1[v3]
            for v2 in reversed(range(a2 + 1)):
                v4[v2][v3] = max(v4[v2][v3], v6[v2 - 1] if v2 - 1 >= 0 else 0) + 1
                v6[v2] = max(v6[v2], v4[v2][v3])
        return v6[a2]

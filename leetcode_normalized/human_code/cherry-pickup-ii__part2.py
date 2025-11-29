import itertools

class C1(object):

    def cherryPickup(self, a1):
        """
        """
        v1 = [[[float('-inf')] * len(a1[0]) for v2 in range(len(a1[0]))] for v2 in range(2)]
        v1[0][0][len(a1[0]) - 1] = a1[0][0] + a1[0][len(a1[0]) - 1]
        for v3 in range(1, len(a1)):
            for v4 in range(len(a1[0])):
                for v5 in range(len(a1[0])):
                    v1[v3 % 2][v4][v5] = max((v1[(v3 - 1) % 2][v4 + d1][v5 + d2] for v6 in range(-1, 2) for v7 in range(-1, 2) if 0 <= v4 + v6 < len(a1[0]) and 0 <= v5 + v7 < len(a1[0]))) + (a1[v3][v4] + a1[v3][v5] if v4 != v5 else a1[v3][v4])
        return max(map(max, *v1[(len(a1) - 1) % 2]))

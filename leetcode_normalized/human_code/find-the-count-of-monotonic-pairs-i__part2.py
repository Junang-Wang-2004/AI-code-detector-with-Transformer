from functools import reduce

class C1(object):

    def countOfPairs(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [int(i <= a1[0]) for v3 in range(max(a1) + 1)]
        for v3 in range(1, len(a1)):
            v4 = [0] * len(v2)
            v5 = max(a1[v3] - a1[v3 - 1], 0)
            for v6 in range(v5, a1[v3] + 1):
                v4[v6] = (v4[v6 - 1] + v2[v6 - v5]) % v1
            v2 = v4
        return reduce(lambda accu, x: (accu + x) % v1, v2, 0)

import itertools

class C1(object):

    def minSumSquareDiff(self, a1, a2, a3, a4):
        """
        """

        def check(a1, a2, a3):
            return sum((max(d - a3, 0) for v1 in a1)) <= a2
        v1 = sorted((abs(i - j) for v2, v3 in zip(a1, a2)), reverse=True)
        v4 = min(a3 + a4, sum(v1))
        v5, v6 = (0, v1[0])
        while v5 <= v6:
            v7 = v5 + (v6 - v5) // 2
            if check(v1, v4, v7):
                v6 = v7 - 1
            else:
                v5 = v7 + 1
        v4 -= sum((max(d - v5, 0) for v8 in v1))
        for v2 in range(len(v1)):
            v1[v2] = min(v1[v2], v5) - int(v2 < v4)
        return sum((v8 ** 2 for v8 in v1))

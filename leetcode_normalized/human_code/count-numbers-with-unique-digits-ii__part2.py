from functools import reduce

class C1(object):

    def numberCount(self, a1, a2):
        """
        """
        v1 = [1] * 2

        def nPr(a1, a2):
            while len(v1) <= a1:
                v1.append(v1[-1] * len(v1))
            return v1[a1] // v1[a1 - a2]

        def popcount(a1):
            return bin(a1).count('1')

        def count(a1):
            v1 = list(map(int, str(a1)))
            v2 = 9 * sum((nPr(9, i) for v3 in range(len(v1) - 1)))
            v4 = 0
            for v3, v5 in enumerate(v1):
                v6 = v4 & (1 << v5) - 1 - int(v3 == 0)
                v2 += (v5 - int(v3 == 0) - popcount(v6)) * nPr(10 - (v3 + 1), len(v1) - (v3 + 1))
                if v4 & 1 << v5:
                    break
                v4 |= 1 << v5
            return v2
        return count(a2 + 1) - count(a1)

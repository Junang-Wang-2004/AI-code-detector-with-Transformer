from functools import reduce

class C1(object):

    def maxSum(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = max(a1).bit_length()
        v3 = [0] * v2
        for v4 in range(v2):
            for v5 in a1:
                if v5 & 1 << v4:
                    v3[v4] += 1
        return reduce(lambda x, y: (v5 + y) % v1, (sum((1 << v4 for v4 in range(v2) if v3[v4] >= j)) ** 2 for v6 in range(1, a2 + 1)))

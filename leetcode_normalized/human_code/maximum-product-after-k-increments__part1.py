class C1(object):

    def maximumProduct(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = sum(a1)
        for v3 in reversed(range(len(a1))):
            if a1[v3] * (v3 + 1) - v2 <= a2:
                break
            v2 -= a1[v3]
        v4, v5 = divmod(a2 + v2, v3 + 1)
        return pow(v4, v3 + 1 - v5, v1) * pow(v4 + 1, v5, v1) * reduce(lambda x, y: x * y % v1, (a1[j] for v6 in range(v3 + 1, len(a1))), 1) % v1

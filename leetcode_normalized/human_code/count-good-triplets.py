class C1(object):

    def countGoodTriplets(self, a1, a2, a3, a4):
        """
        """
        return sum((abs(a1[i] - a1[j]) <= a2 and abs(a1[j] - a1[k]) <= a3 and (abs(a1[k] - a1[i]) <= a4) for v1 in range(len(a1) - 2) for v2 in range(v1 + 1, len(a1) - 1) for v3 in range(v2 + 1, len(a1))))

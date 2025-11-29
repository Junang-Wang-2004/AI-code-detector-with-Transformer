class C1(object):

    def minSwaps(self, a1):
        """
        """

        def count(a1):
            v1 = iter((j for v2 in range(a1, len(a1), 2)))
            return sum((abs(next(v1) - i) for v3 in range(len(a1)) if a1[v3] % 2))
        v1 = sum((x % 2 for v2 in a1))
        if v1 == len(a1) - v1:
            return min(count(0), count(1))
        if v1 == len(a1) - v1 + 1:
            return count(0)
        if v1 + 1 == len(a1) - v1:
            return count(1)
        return -1

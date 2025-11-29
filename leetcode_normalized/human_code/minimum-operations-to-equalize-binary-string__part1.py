class C1(object):

    def minOperations(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = a1.count('0')
        if len(a1) == a2:
            return 0 if v1 == 0 else 1 if v1 == len(a1) else -1
        v2 = float('inf')
        if a2 & 1 == v1 & 1:
            v3 = max(ceil_divide(v1, a2), ceil_divide(len(a1) - v1, len(a1) - a2))
            if v3 & 1 == 0:
                v3 += 1
            v2 = min(v2, v3)
        if v1 & 1 == 0:
            v3 = max(ceil_divide(v1, a2), ceil_divide(v1, len(a1) - a2))
            if v3 & 1 == 1:
                v3 += 1
            v2 = min(v2, v3)
        return v2 if v2 != float('inf') else -1

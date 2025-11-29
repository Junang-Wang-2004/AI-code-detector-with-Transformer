class C1(object):

    def minOperations(self, a1, a2):
        """
        """

        def floor_log2_x(a1):
            return a1.bit_length() - 1
        v1 = sum(a1)
        if v1 < a2:
            return -1
        v2 = [0] * (floor_log2_x(max(a1)) + 1)
        for v3 in a1:
            v2[floor_log2_x(v3)] += 1
        v4 = 0
        for v5 in reversed(range(len(v2))):
            for v6 in range(v2[v5]):
                v3 = 1 << v5
                if v3 <= a2:
                    a2 -= v3
                    v1 -= v3
                elif v1 - v3 >= a2:
                    v1 -= v3
                else:
                    v2[v5 - 1] += 2
                    v4 += 1
        return v4

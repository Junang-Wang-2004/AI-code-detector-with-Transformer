class C1(object):

    def findMaximumNumber(self, a1, a2):
        """
        """

        def floor_log2(a1):
            return a1.bit_length() - 1
        v1 = v2 = 0
        while a1 >= v2:
            v3, v4 = (v2, 0)
            while (v3 << a2) + (1 << v4 + a2 - 1) <= a1:
                v3 = (v3 << a2) + (1 << v4 + a2 - 1)
                v4 += a2
            v5 = min(floor_log2(a1 // v3) if v3 else float('inf'), a2 - 1)
            v3 <<= v5
            v4 += v5
            a1 -= v3
            v1 += 1 << v4
            v2 += int((v4 + 1) % a2 == 0)
        return v1 - 1

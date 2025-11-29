class C1(object):

    def minOperations(self, a1, a2):
        """
        """

        def floor_log2_x(a1):
            return a1.bit_length() - 1
        if sum(a1) < a2:
            return -1
        v1 = [0] * (floor_log2_x(max(a1)) + 1)
        for v2 in a1:
            v1[floor_log2_x(v2)] += 1
        v3 = v4 = 0
        while v4 < len(v1):
            if a2 & 1 << v4:
                if not v1[v4]:
                    v5 = next((v5 for v5 in range(v4, len(v1)) if v1[v5]))
                    v3 += v5 - v4
                    v5 = v4
                    v1[v4] -= 1
                    continue
                v1[v4] -= 1
            if v4 + 1 < len(v1):
                v1[v4 + 1] += v1[v4] // 2
            v4 += 1
        return v3

class C1(object):

    def minOperations(self, a1, a2):
        v1 = len(a1)
        v2 = sum((c == '0' for v3 in a1))
        v4 = v1 - v2
        for v5 in range(v1 + 1):
            v6 = v5 * a2
            if v6 < v2 or (v6 - v2) % 2 != 0:
                continue
            if v5 % 2 == 0:
                v7 = v2 * (v5 - 1) + v4 * v5
            else:
                v7 = v2 * v5 + v4 * (v5 - 1)
            if v6 <= v7:
                return v5
        return -1

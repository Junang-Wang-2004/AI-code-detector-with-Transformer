class C1(object):

    def incremovableSubarrayCount(self, a1):
        v1 = len(a1)
        v2 = 0
        while v2 + 1 < v1 and a1[v2] < a1[v2 + 1]:
            v2 += 1
        if v2 + 1 == v1:
            return v1 * (v1 + 1) // 2
        v3 = v1 - 1
        while v3 - 1 >= 0 and a1[v3 - 1] < a1[v3]:
            v3 -= 1
        v4 = 0
        v5 = v3
        v4 += v1 - v5 + 1
        for v6 in range(v2 + 1):
            while v5 < v1 and a1[v6] >= a1[v5]:
                v5 += 1
            v4 += v1 - v5 + 1
        return v4

class C1:

    def kthSmallestSubarraySum(self, a1, a2):

        def can_achieve(a1):
            v1 = 0
            v2 = 0
            v3 = 0
            for v4 in range(len(a1)):
                v1 += a1[v4]
                while v1 > a1:
                    v1 -= a1[v2]
                    v2 += 1
                v3 += v4 - v2 + 1
            return v3 >= a2
        v1 = min(a1)
        v2 = sum(a1)
        while v1 < v2:
            v3 = v1 + (v2 - v1) // 2
            if can_achieve(v3):
                v2 = v3
            else:
                v1 = v3 + 1
        return v1

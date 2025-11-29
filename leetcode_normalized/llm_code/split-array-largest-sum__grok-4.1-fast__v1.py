class C1:

    def splitArray(self, a1, a2):

        def can_partition(a1):
            v1 = 1
            v2 = 0
            for v3 in a1:
                if v2 + v3 > a1:
                    v1 += 1
                    v2 = v3
                else:
                    v2 += v3
            return v1 <= a2
        v1 = max(a1)
        v2 = sum(a1)
        v3 = v1
        v4 = v2
        while v3 < v4:
            v5 = (v3 + v4) // 2
            if can_partition(v5):
                v4 = v5
            else:
                v3 = v5 + 1
        return v3

class C1:

    def hIndex(self, a1):
        a1.sort()
        v1 = len(a1)
        from bisect import bisect_left
        v2, v3 = (0, v1)
        while v2 < v3:
            v4 = (v2 + v3 + 1) // 2
            v5 = v1 - bisect_left(a1, v4)
            if v5 >= v4:
                v2 = v4
            else:
                v3 = v4 - 1
        return v2

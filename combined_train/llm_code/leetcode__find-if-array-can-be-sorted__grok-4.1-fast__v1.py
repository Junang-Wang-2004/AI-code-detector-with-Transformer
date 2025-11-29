class C1:

    def canSortArray(self, a1):

        def bitcount(a1):
            v1 = 0
            while a1:
                v1 += a1 & 1
                a1 >>= 1
            return v1
        v1 = [bitcount(x) for v2 in a1]
        v3 = len(a1)
        v4 = 0
        v5 = float('-inf')
        while v4 < v3:
            v6 = v4
            while v6 < v3 and v1[v6] == v1[v4]:
                v6 += 1
            v7 = min(a1[v4:v6])
            if v5 > v7:
                return False
            v5 = max(a1[v4:v6])
            v4 = v6
        return True

class C1:

    def smallestDivisor(self, a1, a2):

        def valid(a1, a2, a3):
            v1 = 0
            for v2 in a2:
                v1 += (v2 + a1 - 1) // a1
                if v1 > a3:
                    return False
            return v1 <= a3
        v1 = 1
        v2 = max(a1)
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if valid(v3, a1, a2):
                v2 = v3
            else:
                v1 = v3 + 1
        return v1

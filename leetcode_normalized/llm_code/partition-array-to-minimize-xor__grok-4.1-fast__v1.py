class C1:

    def minXor(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] ^ a1[v3]

        def feasible(a1):
            v1 = 0
            v2 = 0
            while v2 < v1:
                v1 += 1
                if v1 > a2:
                    return False
                v3 = v2[v2]
                v4 = v2
                while v4 < v1 and v2[v4 + 1] ^ v3 <= a1:
                    v4 += 1
                if v4 == v2:
                    return False
                v2 = v4
            return True
        v4 = 0
        v5 = (1 << 31) - 1
        while v4 < v5:
            v6 = (v4 + v5) // 2
            if feasible(v6):
                v5 = v6
            else:
                v4 = v6 + 1
        return v4

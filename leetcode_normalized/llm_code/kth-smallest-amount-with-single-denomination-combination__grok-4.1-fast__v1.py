class C1(object):

    def findKthSmallest(self, a1, a2):

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = len(a1)
        v2 = min(a1)
        v3 = []
        for v4 in range(1, 1 << v1):
            v5 = 1
            v6 = 0
            for v7 in range(v1):
                if v4 & 1 << v7:
                    v5 = v5 * a1[v7] // gcd(v5, a1[v7])
                    v6 += 1
            v8 = 1 if v6 % 2 == 1 else -1
            v3.append((v5, v8))

        def feasible(a1):
            v1 = 0
            for v2, v3 in v3:
                v1 += v3 * (a1 // v2)
            return v1 >= a2
        v9, v10 = (v2, a2 * v2)
        while v9 < v10:
            v11 = (v9 + v10) // 2
            if feasible(v11):
                v10 = v11
            else:
                v9 = v11 + 1
        return v9

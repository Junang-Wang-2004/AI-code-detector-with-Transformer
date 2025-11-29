from math import gcd

class C1:

    def numberOfSubsequences(self, a1):
        v1 = len(a1)
        v2 = {}
        v3 = 0
        for v4 in range(4, v1 - 1):
            v5 = v4 - 2
            for v6 in range(v5 - 1):
                v7 = a1[v6]
                v8 = a1[v5]
                v9 = gcd(v7, v8)
                v10 = (v7 // v9, v8 // v9)
                v2[v10] = v2.get(v10, 0) + 1
            for v11 in range(v4 + 2, v1):
                v12 = a1[v11]
                v13 = a1[v4]
                v9 = gcd(v12, v13)
                v10 = (v12 // v9, v13 // v9)
                v3 += v2.get(v10, 0)
        return v3

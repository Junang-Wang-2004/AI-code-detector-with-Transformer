class C1:

    def divisibleTripletCount(self, a1, a2):
        v1 = {}
        v2 = 0
        v3 = len(a1)
        for v4 in range(v3):
            v5 = a1[v4] % a2
            v2 += v1.get(v5, 0)
            for v6 in range(v4):
                v7 = (a1[v4] + a1[v6]) % a2
                v8 = -v7 % a2
                v1[v8] = v1.get(v8, 0) + 1
        return v2

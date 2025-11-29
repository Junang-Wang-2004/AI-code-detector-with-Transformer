class C1(object):

    def subarrayGCD(self, a1, a2):

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = 0
        v2 = {}
        for v3 in a1:
            if v3 % a2 != 0:
                v2 = {}
                continue
            v4 = {v3: 1}
            for v5, v6 in v2.items():
                v7 = gcd(v5, v3)
                v4[v7] = v4.get(v7, 0) + v6
            v2 = v4
            v1 += v2.get(a2, 0)
        return v1

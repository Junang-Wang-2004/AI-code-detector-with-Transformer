class C1:

    def replaceNonCoprimes(self, a1):

        def gcd(a1, a2):
            while a2 != 0:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = []
        for v2 in a1:
            v1.append(v2)
            while len(v1) > 1:
                v3 = v1[-2]
                v4 = v1[-1]
                v5 = gcd(v3, v4)
                if v5 == 1:
                    break
                v1.pop()
                v1.pop()
                v1.append(v4 * (v3 // v5))
        return v1

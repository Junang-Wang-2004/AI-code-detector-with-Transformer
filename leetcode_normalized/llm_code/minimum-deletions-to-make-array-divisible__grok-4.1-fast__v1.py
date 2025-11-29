class C1:

    def minOperations(self, a1, a2):

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        if not a2:
            return -1
        v1 = a2[0]
        for v2 in a2[1:]:
            v1 = gcd(v1, v2)
            if v1 == 1:
                break
        a1.sort()
        for v3, v4 in enumerate(a1):
            if v1 % v4 == 0:
                return v3
        return -1

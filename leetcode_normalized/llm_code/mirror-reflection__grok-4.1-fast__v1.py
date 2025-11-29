class C1:

    def mirrorReflection(self, a1, a2):

        def valuation(a1):
            v1 = 0
            while a1 % 2 == 0:
                a1 //= 2
                v1 += 1
            return v1
        v1 = valuation(a1)
        v2 = valuation(a2)
        if v1 > v2:
            return 2
        elif v1 < v2:
            return 0
        else:
            return 1

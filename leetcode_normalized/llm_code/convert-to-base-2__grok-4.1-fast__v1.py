class C1:

    def baseNeg2(self, a1):
        v1 = ''
        while a1:
            v2 = a1 % 2
            v1 = str(v2) + v1
            a1 = (a1 - v2) // -2
        return v1 or '0'

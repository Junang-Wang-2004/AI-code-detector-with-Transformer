class C1:

    def convertToBase7(self, a1):
        if a1 == 0:
            return '0'
        v1 = '-' if a1 < 0 else ''
        v2 = abs(a1)
        v3 = []
        while v2 > 0:
            v3.append(str(v2 % 7))
            v2 //= 7
        return v1 + ''.join(reversed(v3))

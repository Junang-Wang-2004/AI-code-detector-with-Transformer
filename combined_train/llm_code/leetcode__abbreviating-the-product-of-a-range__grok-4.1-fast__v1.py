import math

class C1(object):

    def abbreviateProduct(self, a1, a2):
        v1 = v2 = 5
        v3 = 10 ** (v1 + v2)
        v4 = 1
        v5 = 0
        v6 = False
        for v7 in range(a1, a2 + 1):
            v4 *= v7
            while v4 % 10 == 0:
                v4 //= 10
                v5 += 1
            if v4 >= v3:
                v6 = True
                v4 %= v3
        if not v6:
            return f'{v4}e{v5}'
        v8 = 0.0
        for v7 in range(a1, a2 + 1):
            v8 = (v8 + math.log10(v7)) % 1
        v9 = 10 ** v8
        v10 = int(v9 * 10 ** (v1 - 1))
        v11 = str(v10)
        v12 = v4 % 10 ** v2
        v13 = f'{v12:0{v2}d}'
        return f'{v11}...{v13}e{v5}'

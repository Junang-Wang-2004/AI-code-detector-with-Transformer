class C1:

    def fractionToDecimal(self, a1, a2):
        if a1 == 0:
            return '0'
        v1 = (a1 < 0) ^ (a2 < 0)
        v2, v3 = (abs(a1), abs(a2))
        v4 = [str(v2 // v3)]
        v5 = v2 % v3
        if v5:
            v4.append('.')
            v6 = {}
            v7 = []
            v8 = 0
            while v5 and v5 not in v6:
                v6[v5] = v8
                v5 *= 10
                v7.append(str(v5 // v3))
                v5 %= v3
                v8 += 1
            if v5 in v6:
                v9 = v6[v5]
                v7 = v7[:v9] + ['('] + v7[v9:] + [')']
            v4.extend(v7)
        v10 = ''.join(v4)
        return '-' + v10 if v1 else v10

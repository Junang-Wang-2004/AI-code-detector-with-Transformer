class C1:

    def calPoints(self, a1):
        v1 = []
        v2 = 0
        for v3 in a1:
            if v3 == '+':
                v4 = v1[-1] + v1[-2]
                v1.append(v4)
                v2 += v4
            elif v3 == 'D':
                v4 = v1[-1] * 2
                v1.append(v4)
                v2 += v4
            elif v3 == 'C':
                v5 = v1.pop()
                v2 -= v5
            else:
                v4 = int(v3)
                v1.append(v4)
                v2 += v4
        return v2

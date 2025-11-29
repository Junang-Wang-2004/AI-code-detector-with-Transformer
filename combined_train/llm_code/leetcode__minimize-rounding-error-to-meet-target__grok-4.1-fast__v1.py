import math

class C1:

    def minimizeError(self, a1, a2):
        v1 = 0
        v2 = []
        v3 = 0
        for v4 in a1:
            v5 = float(v4)
            v6 = int(v5)
            v1 += v6
            v7 = v5 - v6
            if v7 > 0:
                v2.append(v7)
                v3 += 1
        v8 = v1 + v3
        if v1 > a2 or v8 < a2:
            return '-1'
        v9 = a2 - v1
        v10 = v3 - v9
        v2.sort()
        v11 = sum(v2[:v10])
        for v12 in range(v10, v3):
            v11 += 1 - v2[v12]
        return f'{v11:.3f}'

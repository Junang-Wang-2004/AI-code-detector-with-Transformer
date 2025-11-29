class C1(object):

    def leastOpsExpressTarget(self, a1, a2):
        v1 = []
        v2 = a2
        while v2:
            v1.append(v2 % a1)
            v2 //= a1
        v3 = 0
        v4 = 0
        v5 = 0
        for v6 in v1:
            if v5 == 0:
                v3 = 2 * v6
                v4 = 2 * (a1 - v6)
            else:
                v7 = min(v6 * v5 + v3, (v6 + 1) * v5 + v4)
                v8 = min((a1 - v6) * v5 + v3, (a1 - v6 - 1) * v5 + v4)
                v3 = v7
                v4 = v8
            v5 += 1
        return min(v3, v5 + v4) - 1

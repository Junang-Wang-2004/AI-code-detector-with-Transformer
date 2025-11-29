class C1(object):

    def minDamage(self, a1, a2, a3):
        v1 = sorted((((a3[i] + a1 - 1) // a1 / a2[i], (a3[i] + a1 - 1) // a1, a2[i]) for v2 in range(len(a3))))
        v3 = 0
        v4 = 0
        for v5, v6, v7 in v1:
            v4 += v6
            v3 += v4 * v7
        return v3

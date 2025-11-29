class C1(object):

    def countGoodStrings(self, a1, a2, a3, a4):
        v1 = 10 ** 9 + 7
        v2 = [0] * (a2 + 1)
        v2[0] = 1
        for v3 in range(1, a2 + 1):
            if v3 >= a3:
                v2[v3] = (v2[v3] + v2[v3 - a3]) % v1
            if v3 >= a4:
                v2[v3] = (v2[v3] + v2[v3 - a4]) % v1
        return sum(v2[a1:]) % v1

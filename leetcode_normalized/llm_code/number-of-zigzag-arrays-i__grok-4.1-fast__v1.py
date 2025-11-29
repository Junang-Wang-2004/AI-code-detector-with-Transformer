class C1(object):

    def zigZagArrays(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = a3 - a2 + 1
        v3 = [1] * v2
        for v4 in range(a1 - 1):
            v5 = [0] * (v2 + 1)
            for v6 in range(v2):
                v5[v6 + 1] = (v5[v6] + v3[v6]) % v1
            v3 = v5[:v2][::-1]
        return sum(v3) * 2 % v1

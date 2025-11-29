v1 = 10 ** 9 + 7
v2 = 1000
v3 = [0] * (2 * v2 - 1 + 1)
v4 = [0] * (2 * v2 - 1 + 1)
v5 = [0] * (2 * v2 - 1 + 1)
v3[0] = v5[0] = v3[1] = v5[1] = v4[1] = 1
for v6 in range(2, len(v3)):
    v3[v6] = v3[v6 - 1] * v6 % v1
    v4[v6] = v4[v1 % v6] * (v1 - v1 // v6) % v1
    v5[v6] = v5[v6 - 1] * v4[v6] % v1

class C1(object):

    def numberOfSets(self, a1, a2):
        """
        """

        def nCr(a1, a2, a3):
            return v3[a1] * v5[a1 - a2] % a3 * v5[a2] % a3
        return nCr(a1 + a2 - 1, 2 * a2, v1)

class C1(object):

    def numberOfWays(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4 = [[1] * 2 for v5 in range(3)]

        def nCr(a1, a2):
            while len(v3) <= a1:
                v2.append(v2[-1] * len(v3) % v1)
                v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
                v4.append(v4[-1] * v3[-1] % v1)
            return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1
        v6 = a3 - abs(a2 - a1)
        return nCr(a3, v6 // 2) if v6 >= 0 and v6 % 2 == 0 else 0

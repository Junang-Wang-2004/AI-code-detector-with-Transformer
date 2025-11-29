class C1(object):

    def countNumbers(self, a1, a2, a3):
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

        def nHr(a1, a2):
            return nCr(a1 + a2 - 1, a2)

        def count(a1):
            v1 = []
            while a1:
                a1, v3 = divmod(a1, a3)
                v1.append(v3)
            v1.reverse()
            if not v1:
                v1.append(0)
            v4 = 0
            for v5 in range(len(v1)):
                if v5 - 1 >= 0 and v1[v5 - 1] > v1[v5]:
                    break
                for v6 in range(v1[v5 - 1] if v5 - 1 >= 0 else 0, v1[v5]):
                    v4 = (v4 + nHr(a3 - 1 - v6 + 1, len(v1) - (v5 + 1))) % v1
            else:
                v4 = (v4 + 1) % v1
            return v4
        return (count(int(a2)) - count(int(a1) - 1)) % v1

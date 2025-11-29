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

        def decrease(a1):
            for v1 in reversed(range(len(a1))):
                if a1[v1]:
                    a1[v1] -= 1
                    break
                a1[v1] = 9

        def divide(a1, a2):
            v1 = []
            v2 = 0
            for v3 in a1:
                v4, v2 = divmod(v2 * 10 + v3, a2)
                if v1 or v4:
                    v1.append(v4)
            return (v1, v2)

        def to_base(a1, a2):
            v1 = []
            while a1:
                a1, v3 = divide(a1, a2)
                v1.append(v3)
            v1.reverse()
            return v1

        def count(a1):
            v1 = to_base(a1, a3)
            v2 = 0
            for v3 in range(len(v1)):
                if v3 - 1 >= 0 and v1[v3 - 1] > v1[v3]:
                    break
                for v4 in range(v1[v3 - 1] if v3 - 1 >= 0 else 0, v1[v3]):
                    v2 = (v2 + nHr(a3 - 1 - v4 + 1, len(v1) - (v3 + 1))) % v1
            else:
                v2 = (v2 + 1) % v1
            return v2
        v6 = list(map(int, a1))
        decrease(v6)
        v7 = list(map(int, a2))
        return (count(v7) - count(v6)) % v1

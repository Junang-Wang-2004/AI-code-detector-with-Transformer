from functools import reduce
v1 = [0] * 2

class C1(object):

    def countKReducibleNumbers(self, a1, a2):
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

        def popcount(a1):
            return bin(a1).count('1')
        while len(a1) - 1 >= len(v1):
            v1.append(v1[popcount(len(v1))] + 1)
        v6 = v7 = 0
        for v8 in range(len(a1)):
            if a1[v8] != '1':
                continue
            for v9 in range(len(a1) - (v8 + 1) + 1):
                if v1[v7 + v9] < a2:
                    v6 = (v6 + nCr(len(a1) - (v8 + 1), v9)) % v1
            v7 += 1
        return (v6 - 1) % v1

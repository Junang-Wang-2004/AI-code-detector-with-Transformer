from functools import reduce
v1 = 10 ** 9 + 7
v2, v3, v4 = [[1] * 2 for v5 in range(3)]

def f1(a1, a2):
    if a1 < a2:
        return 0
    while len(v3) <= a1:
        v2.append(v2[-1] * len(v3) % v1)
        v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
        v4.append(v4[-1] * v3[-1] % v1)
    return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1

class C1(object):

    def minMaxSums(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = 0
        v3 = 1
        for v4 in range(len(a1)):
            v2 = (v2 + (a1[v4] + a1[~v4]) * v3) % v1
            v3 = (v3 * 2 - f1(v4, a2 - 1)) % v1
        return v2

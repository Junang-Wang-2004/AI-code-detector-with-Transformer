from functools import reduce
v1 = 10 ** 9 + 7

class C1(object):

    def __init__(self, a1):
        self.__bit = [0] * (a1 + 1)

    def add(self, a1, a2):
        a1 += 1
        while a1 < len(self.__bit):
            self.__bit[a1] = (self.__bit[a1] + a2) % v1
            a1 += a1 & -a1

    def query(self, a1):
        a1 += 1
        v2 = 0
        while a1 > 0:
            v2 = (v2 + self.__bit[a1]) % v1
            a1 -= a1 & -a1
        return v2

def f3(a1):
    v1 = [[] for v2 in range(a1 + 1)]
    for v3 in range(1, a1 + 1):
        for v4 in range(v3, a1 + 1, v3):
            v1[v4].append(v3)
    return v1

def f4(a1):
    v1 = list(range(a1 + 1))
    for v2 in range(2, a1 + 1):
        if v1[v2] != v2:
            continue
        for v3 in range(v2, a1 + 1, v2):
            v1[v3] -= v1[v3] // v2
    return v1
v2 = 7 * 10 ** 4
v3 = f3(v2)
v4 = f4(v2)

class C2(object):

    def totalBeauty(self, a1):
        """
        """

        def count(a1):
            for v1, v2 in enumerate(sorted(a1)):
                val_to_idx[v2] = v1
            v3 = C1(len(a1))
            for v2 in a1:
                v3.add(val_to_idx[v2], v3.query(val_to_idx[v2] - 1) + 1)
            return v3.query(len(a1) - 1)
        v1 = max(a1)
        v2 = [0] * (v1 + 1)
        v3 = [[] for v4 in range(v1 + 1)]
        for v5 in a1:
            for v6 in v3[v5]:
                v3[v6].append(v5)
        return reduce(lambda accu, x: (accu + v5) % v1, (v4[g] * count(v3[g]) for v7 in reversed(range(1, v1 + 1))), 0)

def f1(a1):
    return bin(a1).count('1')

def f2(a1):
    return (a1 - 1).bit_length()

class C1(object):

    def __init__(self, a1):
        self.__bit = [0] * (a1 + 1)

    def add(self, a1, a2):
        a1 += 1
        while a1 < len(self.__bit):
            self.__bit[a1] += a2
            a1 += a1 & -a1

    def query(self, a1):
        a1 += 1
        v2 = 0
        while a1 > 0:
            v2 += self.__bit[a1]
            a1 -= a1 & -a1
        return v2
v1 = 10 ** 15
v2 = v1.bit_length()
v3 = [0] * (v2 + 1)
for v4 in range(2, v2 + 1):
    v3[v4] = v3[f1(v4)] + 1
v5 = 0
while v1 != 1:
    v1 = f2(v1)
    v5 += 1

class C2(object):

    def popcountDepth(self, a1, a2):
        """
        """

        def count(a1):
            return v3[f1(a1)] + 1 if a1 != 1 else 0
        v1 = [C1(len(a1)) for v2 in range(v5 + 1)]
        for v3 in range(len(a1)):
            v1[count(a1[v3])].add(v3, +1)
        v4 = []
        for v5 in a2:
            if v5[0] == 1:
                v2, v6, v7, v8 = v5
                assert v8 < len(v1)
                v4.append(v1[v8].query(v7) - v1[v8].query(v6 - 1))
            else:
                v2, v3, v9 = v5
                v10 = count(a1[v3])
                v11 = count(v9)
                if v11 != v10:
                    v1[v10].add(v3, -1)
                    v1[v11].add(v3, +1)
                a1[v3] = v9
        return v4

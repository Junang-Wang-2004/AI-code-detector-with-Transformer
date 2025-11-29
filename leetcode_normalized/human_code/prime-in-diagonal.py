def f1(a1):
    v1 = []
    v2 = [-1] * (a1 + 1)
    for v3 in range(2, a1 + 1):
        if v2[v3] == -1:
            v2[v3] = v3
            v1.append(v3)
        for v4 in v1:
            if v3 * v4 > a1 or v4 > v2[v3]:
                break
            v2[v3 * v4] = v4
    return v1
v1 = 4 * 10 ** 6
v2 = f1(v1)
v3 = set(v2)

class C1(object):

    def diagonalPrime(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v2][v2] in v3:
                v1 = max(v1, a1[v2][v2])
            if a1[v2][~v2] in v3:
                v1 = max(v1, a1[v2][~v2])
        return v1

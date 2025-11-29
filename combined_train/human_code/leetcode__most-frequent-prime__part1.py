import collections

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
    return v2
v1 = 6
v2 = f1(10 ** v1 - 1)

class C1(object):

    def mostFrequentPrime(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

        def numbers(a1, a2, a3, a4):
            v1 = 0
            while 0 <= a1 < len(a1) and 0 <= a2 < len(a1[0]):
                v1 = v1 * 10 + a1[a1][a2]
                yield v1
                a1, a2 = (a1 + a3, a2 + a4)
        v2 = collections.Counter((x for v3 in range(len(a1)) for v4 in range(len(a1[0])) for v5, v6 in v1 for v7 in numbers(v3, v4, v5, v6) if v7 > 10 and v2[v7] == v7))
        v2[-1] = 0
        return max(iter(v2.keys()), key=lambda x: (v2[v7], v7))

import collections

def f1(a1):
    if a1 % 2 == 0 or a1 % 3 == 0:
        return False
    for v1 in range(5, a1, 6):
        if v1 * v1 > a1:
            break
        if a1 % v1 == 0 or a1 % (v1 + 2) == 0:
            return False
    return True

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
        v2 = collections.Counter((x for v3 in range(len(a1)) for v4 in range(len(a1[0])) for v5, v6 in v1 for v7 in numbers(v3, v4, v5, v6) if v7 > 10))
        v2[-1] = 0
        return max((p for v8 in v2.keys() if f1(v8) or v8 == -1), key=lambda x: (v2[v7], v7))

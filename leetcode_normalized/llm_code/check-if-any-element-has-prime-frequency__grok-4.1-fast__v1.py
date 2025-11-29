import collections

def f1(a1):
    v1 = [True] * (a1 + 1)
    v1[0] = v1[1] = False
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if v1[v2]:
            for v3 in range(v2 * v2, a1 + 1, v2):
                v1[v3] = False
    return {v2 for v2 in range(2, a1 + 1) if v1[v2]}
v1 = 100
v2 = f1(v1)

class C1(object):

    def checkPrimeFrequency(self, a1):
        v1 = collections.Counter(a1)
        return any((freq in v2 for v2 in v1.values()))

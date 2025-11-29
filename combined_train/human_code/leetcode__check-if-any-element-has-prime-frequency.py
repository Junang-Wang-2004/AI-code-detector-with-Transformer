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
v1 = 100
v2 = f1(v1)

class C1(object):

    def checkPrimeFrequency(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2] += 1
        return any((v2[v] == v for v3 in v1.values()))

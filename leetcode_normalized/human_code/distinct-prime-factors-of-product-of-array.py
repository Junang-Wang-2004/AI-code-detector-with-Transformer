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
v1 = 10 ** 3
v2 = f1(int(v1 ** 0.5))

class C1(object):

    def distinctPrimeFactors(self, a1):
        """
        """
        v1 = set()
        for v2 in set(a1):
            for v3 in v2:
                if v3 > v2:
                    break
                if v2 % v3:
                    continue
                v1.add(v3)
                while v2 % v3 == 0:
                    v2 //= v3
            if v2 != 1:
                v1.add(v2)
        return len(v1)

import bisect

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
v2 = f1(v1 - 1)

class C1(object):

    def primeSubOperation(self, a1):
        """
        """
        for v1 in range(len(a1)):
            v2 = bisect.bisect_left(v2, a1[v1] - a1[v1 - 1] if v1 - 1 >= 0 else a1[v1])
            if v2 - 1 >= 0:
                a1[v1] -= v2[v2 - 1]
            if v1 - 1 >= 0 and a1[v1 - 1] >= a1[v1]:
                return False
        return True

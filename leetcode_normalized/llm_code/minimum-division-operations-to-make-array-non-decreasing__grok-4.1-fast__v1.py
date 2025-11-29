def f1(a1):
    v1 = list(range(a1 + 1))
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if v1[v2] == v2:
            for v3 in range(v2 * v2, a1 + 1, v2):
                if v1[v3] == v3:
                    v1[v3] = v2
    return v1
v1 = 10 ** 6 + 10
v2 = f1(v1)

class C1(object):

    def minOperations(self, a1):
        if not a1:
            return 0
        v1 = 0
        v2 = a1[-1]
        for v3 in range(len(a1) - 2, -1, -1):
            v4 = a1[v3]
            if v4 <= v2:
                v2 = v4
            else:
                v5 = v2[v4]
                if v5 > v2:
                    return -1
                v2 = v5
                v1 += 1
        return v1

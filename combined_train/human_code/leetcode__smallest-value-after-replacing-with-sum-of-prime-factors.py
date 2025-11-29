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
v1 = 10 ** 5
v2 = f1(int(v1 ** 0.5))

class C1(object):

    def smallestValue(self, a1):
        """
        """
        while True:
            v1, v2 = (a1, 0)
            for v3 in v2:
                if v3 ** 2 > v1:
                    break
                while v1 % v3 == 0:
                    v1 //= v3
                    v2 += v3
            if v1 > 1:
                v2 += v1
            if v2 == a1:
                break
            a1 = v2
        return a1

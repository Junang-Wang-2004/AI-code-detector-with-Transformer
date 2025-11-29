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
v1 = 10 ** 9
v2 = f1(int(v1 ** 0.5))

class C1(object):

    def nonSpecialCount(self, a1, a2):
        """
        """

        def count(a1):
            return a1 - bisect.bisect_right(v2, int(a1 ** 0.5))
        return count(a2) - count(a1 - 1)

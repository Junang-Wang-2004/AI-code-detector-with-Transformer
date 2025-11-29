class C1(object):

    def isPossible(self, a1):
        v1 = len(a1)
        v2 = sum(a1)
        v3 = sorted(a1, reverse=True)
        while v2 > v1:
            v4 = v3[0]
            v5 = v2 - v4
            if v5 <= 0:
                return False
            v6 = 2 * v4 - v2
            if v6 <= 0:
                return False
            if v6 > v5:
                v6 = v6 % v5 + v5
            v3[0] = v6
            v2 = v6 + v5
            v3.sort(reverse=True)
        return v2 == v1

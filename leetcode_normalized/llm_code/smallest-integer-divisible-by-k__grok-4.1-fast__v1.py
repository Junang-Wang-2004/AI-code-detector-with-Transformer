class C1(object):

    def smallestRepunitDivByK(self, a1):
        if a1 % 2 == 0 or a1 % 5 == 0:
            return -1
        v1 = 0
        v2 = 1
        for v3 in range(1, a1 + 1):
            v1 = (v1 + v2) % a1
            if v1 == 0:
                return v3
            v2 = v2 * 10 % a1
        return -1

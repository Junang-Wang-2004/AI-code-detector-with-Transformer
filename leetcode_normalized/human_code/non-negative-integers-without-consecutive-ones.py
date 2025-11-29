class C1(object):

    def findIntegers(self, a1):
        """
        """
        v1 = [0] * 32
        v1[0], v1[1] = (1, 2)
        for v2 in range(2, len(v1)):
            v1[v2] = v1[v2 - 1] + v1[v2 - 2]
        v3, v4 = (0, 0)
        for v2 in reversed(range(31)):
            if a1 & 1 << v2 != 0:
                v3 += v1[v2]
                if v4 == 1:
                    v3 -= 1
                    break
                v4 = 1
            else:
                v4 = 0
        return v3 + 1

class C1(object):

    def canMakeEqual(self, a1, a2):
        """
        """

        def check(a1):
            v1 = v2 = 0
            for v3 in range(len(a1)):
                if a1[v3] == a1:
                    continue
                v2 += v3 if v1 else -v3
                if v2 > a2:
                    return False
                v1 ^= 1
            return v1 == 0
        return check(1) or check(-1)

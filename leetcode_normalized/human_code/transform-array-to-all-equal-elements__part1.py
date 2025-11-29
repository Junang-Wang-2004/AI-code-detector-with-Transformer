class C1(object):

    def canMakeEqual(self, a1, a2):
        """
        """

        def check(a1):
            v1 = 0
            v2 = 1
            for v3 in range(len(a1)):
                if a1[v3] * v2 == a1:
                    v2 = 1
                    continue
                v1 += 1
                if v3 + 1 == len(a1) or v1 > a2:
                    return False
                v2 = -1
            return True
        return check(1) or check(-1)

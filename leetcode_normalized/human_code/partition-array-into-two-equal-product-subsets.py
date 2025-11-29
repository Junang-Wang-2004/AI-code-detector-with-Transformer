class C1(object):

    def checkEqualPartitions(self, a1, a2):
        """
        """
        v1 = 1
        for v2 in a1:
            v1 *= v2
            if v1 > a2 ** 2:
                return False
        if v1 != a2 ** 2:
            return False
        for v3 in range(1, 1 << len(a1) - 1):
            v4 = 1
            for v5 in range(len(a1)):
                if not v3 & 1 << v5:
                    continue
                v4 *= a1[v5]
                if v4 > a2:
                    break
            if v4 == a2:
                return True
        return False

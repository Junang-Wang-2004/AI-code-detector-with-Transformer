class C1(object):

    def splitString(self, a1):
        v1 = len(a1)

        def helper(a1, a2):
            if a2 < 0:
                return False
            v1 = str(a2)
            v2 = len(v1)
            if a1 + v2 > v1 or a1[a1:a1 + v2] != v1:
                return False
            v3 = a1 + v2
            if v3 == v1:
                return True
            return helper(v3, a2 - 1)
        for v2 in range(1, v1):
            if a1[0] == '0' and v2 > 1:
                continue
            v3 = int(a1[:v2])
            if helper(v2, v3 - 1):
                return True
        return False

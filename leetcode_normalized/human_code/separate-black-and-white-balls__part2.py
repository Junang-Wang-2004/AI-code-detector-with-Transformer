class C1(object):

    def minimumSteps(self, a1):
        """
        """
        v1 = 0
        v2, v3 = (0, len(a1) - 1)
        while v2 < v3:
            if v2 < len(a1) and a1[v2] != '1':
                v2 += 1
                continue
            if v3 >= 0 and a1[v3] != '0':
                v3 -= 1
                continue
            v1 += v3 - v2
            v2 += 1
            v3 -= 1
        return v1

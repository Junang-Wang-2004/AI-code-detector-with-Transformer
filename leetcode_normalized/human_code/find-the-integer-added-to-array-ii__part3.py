class C1(object):

    def minimumAddedInteger(self, a1, a2):
        """
        """
        a1.sort()
        a2.sort()
        for v1 in range(3):
            v2 = a2[-1] - a1[~v1]
            v3 = 0
            for v4 in range(len(a2)):
                while v4 + v3 < len(a1) and a1[v4 + v3] + v2 != a2[v4]:
                    v3 += 1
            if v3 <= 2:
                return v2
        return -1

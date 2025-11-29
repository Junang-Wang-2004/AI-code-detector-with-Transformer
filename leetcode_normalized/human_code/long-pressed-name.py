class C1(object):

    def isLongPressedName(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(len(a2)):
            if v1 < len(a1) and a1[v1] == a2[v2]:
                v1 += 1
            elif v2 == 0 or a2[v2] != a2[v2 - 1]:
                return False
        return v1 == len(a1)

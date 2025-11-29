class C1(object):

    def getCommon(self, a1, a2):
        """
        """
        v1 = v2 = 0
        while v1 < len(a1) and v2 < len(a2):
            if a1[v1] < a2[v2]:
                v1 += 1
            elif a1[v1] > a2[v2]:
                v2 += 1
            else:
                return a1[v1]
        return -1

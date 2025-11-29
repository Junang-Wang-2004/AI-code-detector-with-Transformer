class C1(object):

    def checkPossibility(self, a1):
        """
        """
        v1, v2 = (False, a1[0])
        for v3 in range(1, len(a1)):
            if v2 > a1[v3]:
                if v1:
                    return False
                if v3 - 2 < 0 or a1[v3 - 2] <= a1[v3]:
                    v2 = a1[v3]
                v1 = True
            else:
                v2 = a1[v3]
        return True

class C1(object):

    def catchMaximumAmountofPeople(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        while v2 < len(a1) and v3 < len(a1):
            if v2 + a2 < v3 or a1[v2] != 1:
                v2 += 1
            elif v3 + a2 < v2 or a1[v3] != 0:
                v3 += 1
            else:
                v1 += 1
                v2 += 1
                v3 += 1
        return v1

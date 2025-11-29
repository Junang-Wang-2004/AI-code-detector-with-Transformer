class C1(object):

    def findDuplicate(self, a1):
        """
        """
        v1, v2 = (1, len(a1) - 1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) / 2
            v4 = 0
            for v5 in a1:
                if v5 <= v3:
                    v4 += 1
            if v4 > v3:
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1

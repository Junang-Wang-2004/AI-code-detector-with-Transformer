class C1(object):

    def totalReplacements(self, a1):
        """
        """
        v1 = -1
        v2 = float('inf')
        for v3 in a1:
            if v3 >= v2:
                continue
            v2 = v3
            v1 += 1
        return v1

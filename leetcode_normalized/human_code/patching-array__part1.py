class C1(object):

    def minPatches(self, a1, a2):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 > a2:
                break
            while not v2 >= v3 - 1:
                v1 += 1
                v2 += v2 + 1
            v2 += v3
        while not v2 >= a2:
            v1 += 1
            v2 += v2 + 1
        return v1

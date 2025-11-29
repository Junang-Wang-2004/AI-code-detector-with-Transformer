class C1(object):

    def minPatches(self, a1, a2):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            while not v2 >= v3 - 1:
                v1 += 1
                v2 += v2 + 1
                if v2 >= a2:
                    return v1
            v2 += v3
            if v2 >= a2:
                return v1
        while not v2 >= a2:
            v1 += 1
            v2 += v2 + 1
        return v1

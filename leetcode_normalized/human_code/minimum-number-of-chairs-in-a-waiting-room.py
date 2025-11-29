class C1(object):

    def minimumChairs(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            v2 += +1 if v3 == 'E' else -1
            v1 = max(v1, v2)
        return v1

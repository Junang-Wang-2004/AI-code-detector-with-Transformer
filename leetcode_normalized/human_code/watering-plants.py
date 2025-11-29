class C1(object):

    def wateringPlants(self, a1, a2):
        """
        """
        v1, v2 = (len(a1), a2)
        for v3, v4 in enumerate(a1):
            if v2 < v4:
                v1 += 2 * v3
                v2 = a2
            v2 -= v4
        return v1

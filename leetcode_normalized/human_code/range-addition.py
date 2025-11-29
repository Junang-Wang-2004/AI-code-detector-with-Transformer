class C1(object):

    def getModifiedArray(self, a1, a2):
        """
        """
        v1 = [0] * a1
        for v2 in a2:
            v1[v2[0]] += v2[2]
            if v2[1] + 1 < a1:
                v1[v2[1] + 1] -= v2[2]
        for v3 in range(1, a1):
            v1[v3] += v1[v3 - 1]
        return v1

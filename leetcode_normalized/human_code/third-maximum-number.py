class C1(object):

    def thirdMax(self, a1):
        """
        """
        v1 = 0
        v2 = [float('-inf')] * 3
        for v3 in a1:
            if v3 > v2[0]:
                v2[0], v2[1], v2[2] = (v3, v2[0], v2[1])
                v1 += 1
            elif v3 != v2[0] and v3 > v2[1]:
                v2[1], v2[2] = (v3, v2[1])
                v1 += 1
            elif v3 != v2[0] and v3 != v2[1] and (v3 >= v2[2]):
                v2[2] = v3
                v1 += 1
        if v1 < 3:
            return v2[0]
        return v2[2]

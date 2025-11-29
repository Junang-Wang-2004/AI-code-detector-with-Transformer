class C1(object):

    def maxBalancedShipments(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 < v2:
                v2 = 0
                v1 += 1
            else:
                v2 = v3
        return v1

class C1(object):

    def maxBalancedShipments(self, a1):
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = len(a1)
        while v3 < v4:
            v5 = a1[v3]
            if v5 < v2:
                v1 += 1
                v2 = 0
            else:
                v2 = v5
            v3 += 1
        return v1

class C1(object):

    def maximumProduct(self, a1):
        """
        """
        v1, v2 = (float('inf'), float('inf'))
        v3, v4, v5 = (float('-inf'), float('-inf'), float('-inf'))
        for v6 in a1:
            if v6 <= v1:
                v2 = v1
                v1 = v6
            elif v6 <= v2:
                v2 = v6
            if v6 >= v3:
                v5 = v4
                v4 = v3
                v3 = v6
            elif v6 >= v4:
                v5 = v4
                v4 = v6
            elif v6 >= v5:
                v5 = v6
        return max(v1 * v2 * v3, v3 * v4 * v5)

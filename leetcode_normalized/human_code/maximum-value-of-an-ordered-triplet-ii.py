class C1(object):

    def maximumTripletValue(self, a1):
        """
        """
        v1 = float('-inf')
        v2 = 0
        v3 = v4 = v1
        for v5 in a1:
            if v3 != v1:
                v2 = max(v2, v3 * v5)
            if v4 != v1:
                v3 = max(v3, v4 - v5)
            v4 = max(v4, v5)
        return v2

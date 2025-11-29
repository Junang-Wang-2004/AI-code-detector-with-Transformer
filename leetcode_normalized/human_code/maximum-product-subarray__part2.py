class C1(object):

    def maxProduct(self, a1):
        v1, v2, v3 = (float('-inf'), 1, 1)
        for v4 in a1:
            v2 = max(1, v2)
            if v4 > 0:
                v2, v3 = (v2 * v4, v3 * v4)
            else:
                v2, v3 = (v3 * v4, v2 * v4)
            v1 = max(v1, v2)
        return v1

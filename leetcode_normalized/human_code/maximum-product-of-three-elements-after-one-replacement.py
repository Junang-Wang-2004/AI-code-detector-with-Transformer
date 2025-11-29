class C1(object):

    def maxProduct(self, a1):
        """
        """
        v1 = 2
        v2 = [0] * v1
        for v3 in a1:
            v3 = abs(v3)
            for v4 in range(v1):
                if v3 > v2[v4]:
                    v3, v2[v4] = (v2[v4], v3)
        return v2[0] * v2[1] * 10 ** 5

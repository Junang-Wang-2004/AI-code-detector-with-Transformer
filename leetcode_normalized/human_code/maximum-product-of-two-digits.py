class C1(object):

    def maxProduct(self, a1):
        """
        """
        v1 = 2

        def count(a1):
            v1 = [0] * 10
            while a1:
                a1, v3 = divmod(a1, 10)
                v1[v3] += 1
            return v1
        v2 = count(a1)
        v3 = 1
        v4 = v1
        for v5 in reversed(range(9 + 1)):
            if v4 == 0:
                break
            while v2[v5] and v4:
                v2[v5] -= 1
                v4 -= 1
                v3 *= v5
        return v3

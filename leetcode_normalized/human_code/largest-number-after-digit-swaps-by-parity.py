class C1(object):

    def largestInteger(self, a1):
        """
        """

        def count(a1):
            v1 = [0] * 10
            while a1:
                a1, v3 = divmod(a1, 10)
                v1[v3] += 1
            return v1
        v1 = count(a1)
        v2 = 0
        v3 = [0, 1]
        v4 = 1
        while a1:
            a1, v6 = divmod(a1, 10)
            while not v1[v3[v6 % 2]]:
                v3[v6 % 2] += 2
            v1[v3[v6 % 2]] -= 1
            v2 += v3[v6 % 2] * v4
            v4 *= 10
        return v2

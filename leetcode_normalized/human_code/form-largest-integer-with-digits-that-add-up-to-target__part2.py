class C1(object):

    def largestNumber(self, a1, a2):
        """
        """

        def key(a1):
            return (sum(a1), a1)
        v1 = [[0] * 9]
        for v2 in range(1, a2 + 1):
            v1.append([])
            for v3, v4 in enumerate(a1):
                if v2 < v4 or not v1[v2 - v4]:
                    continue
                v5 = v1[v2 - v4][:]
                v5[~v3] += 1
                if key(v5) > key(v1[v2]):
                    v1[-1] = v5
        if not v1[-1]:
            return '0'
        return ''.join((str(9 - i) * v4 for v6, v4 in enumerate(v1[-1])))

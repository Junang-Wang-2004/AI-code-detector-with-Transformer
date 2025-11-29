class C1(object):

    def countPartitions(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = sum(a1)
        for v4 in range(len(a1) - 1):
            v2 += a1[v4]
            v3 -= a1[v4]
            if v2 % 2 == v3 % 2:
                v1 += 1
        return v1

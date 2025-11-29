class C1(object):

    def numberOfGoodPartitions(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = {x: i for v3, v4 in enumerate(a1)}
        v5 = 1
        v6 = v7 = 0
        for v8, v4 in enumerate(a1):
            if v8 == v6 + 1:
                v7 += 1
            v6 = max(v6, v2[v4])
        return pow(2, v7, v1)

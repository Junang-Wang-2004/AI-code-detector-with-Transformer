class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = [0] * len(a1)
        for v2 in (lambda x: x, reversed):
            v3 = v4 = 0
            for v5 in v2(range(len(a1))):
                v1[v5] += v4
                if a1[v5] == '1':
                    v3 += 1
                v4 += v3
        return v1

class C1(object):

    def numOfSubsequences(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = a1.count('T')
        v4 = v5 = v6 = v7 = 0
        for v8 in a1:
            v4 = max(v4, v1 * v3)
            if v8 == 'L':
                v1 += 1
            elif v8 == 'C':
                v2 += 1
                v6 += v1
            elif v8 == 'T':
                v3 -= 1
                v7 += v2
                v5 += v6
        v9 = max(v4, v1 * v3)
        return v5 + max(v7, v4, v6)

class C1(object):

    def numOfSubsequences(self, a1):
        v1 = a1.count('T')
        v2 = 0
        v3 = 0
        v4 = v1
        for v5 in a1:
            v2 = max(v2, v3 * v4)
            if v5 == 'L':
                v3 += 1
            elif v5 == 'T':
                v4 -= 1
        v3 = 0
        v6 = 0
        v7 = 0
        v8 = 0
        v9 = 0
        for v5 in a1:
            if v5 == 'L':
                v3 += 1
            elif v5 == 'C':
                v7 += v3
                v6 += 1
            else:
                v8 += v6
                v9 += v7
        return v9 + max(v8, v2, v7)

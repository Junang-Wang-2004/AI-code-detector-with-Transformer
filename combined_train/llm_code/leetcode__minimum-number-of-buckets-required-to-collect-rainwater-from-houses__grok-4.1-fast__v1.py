class C1(object):

    def minimumBuckets(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = False
        while v3 < v1:
            if a1[v3] != 'H':
                v4 = False
                v3 += 1
                continue
            if v4:
                v3 += 1
                v4 = False
                continue
            if v3 + 1 < v1 and a1[v3 + 1] == '.':
                v2 += 1
                v3 += 2
                v4 = True
                continue
            if v3 > 0 and a1[v3 - 1] == '.':
                v2 += 1
                v3 += 1
                v4 = False
                continue
            return -1
        return v2

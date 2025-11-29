class C1(object):

    def minimumBuckets(self, a1):
        """
        """
        v1 = 0
        a1 = list(a1)
        for v3, v4 in enumerate(a1):
            if v4 != 'H' or (v3 and a1[v3 - 1] == 'B'):
                continue
            if v3 + 1 < len(a1) and a1[v3 + 1] == '.':
                a1[v3 + 1] = 'B'
                v1 += 1
            elif v3 and a1[v3 - 1] == '.':
                a1[v3 - 1] = 'B'
                v1 += 1
            else:
                return -1
        return v1

class C1(object):

    def minDeletionSize(self, a1):
        if not a1:
            return 0
        v1 = 0
        v2 = len(a1[0])
        for v3 in range(v2):
            v4 = a1[0][v3]
            v5 = True
            for v6 in range(1, len(a1)):
                v7 = a1[v6][v3]
                if v4 > v7:
                    v5 = False
                    break
                v4 = v7
            if not v5:
                v1 += 1
        return v1

class C1(object):

    def minimumPartition(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        while v2 < v1:
            v4 = v2
            v5 = 0
            while v4 < v1:
                v6 = v5 * 10 + int(a1[v4])
                if v6 > a2:
                    break
                v5 = v6
                v4 += 1
            if v4 == v2:
                return -1
            v3 += 1
            v2 = v4
        return v3

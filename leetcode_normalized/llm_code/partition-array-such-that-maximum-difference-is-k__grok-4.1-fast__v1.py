class C1(object):

    def partitionArray(self, a1, a2):
        a1.sort()
        v1, v2 = (0, 0)
        for v3 in range(len(a1)):
            if a1[v3] - a1[v2] > a2:
                v1 += 1
                v2 = v3
        return v1 + 1

class C1(object):

    def getRow(self, a1):
        v1 = [1]
        for v2 in range(1, a1 + 1):
            v1 = [1] + [v1[j - 1] + v1[j] for v3 in range(1, v2)] + [1]
        return v1

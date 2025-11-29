class C1(object):

    def findWinningPlayer(self, a1, a2):
        v1 = 0
        v2 = 0
        v3 = 1
        v4 = len(a1)
        while v3 < v4:
            if a1[v1] >= a1[v3]:
                v2 += 1
            else:
                v1 = v3
                v2 = 1
            if v2 == a2:
                return v1
            v3 += 1
        return v1

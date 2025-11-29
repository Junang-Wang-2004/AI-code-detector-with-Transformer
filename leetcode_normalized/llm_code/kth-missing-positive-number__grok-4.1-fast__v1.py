class C1(object):

    def findKthPositive(self, a1, a2):
        v1 = len(a1)
        v2, v3 = (0, v1)
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if a1[v4] - v4 - 1 < a2:
                v2 = v4 + 1
            else:
                v3 = v4
        return a2 + v2

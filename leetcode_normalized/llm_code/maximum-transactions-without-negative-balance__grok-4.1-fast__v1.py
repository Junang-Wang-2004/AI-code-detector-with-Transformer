class C1(object):

    def maxTransactions(self, a1):
        v1 = sorted(a1, reverse=True)
        v2 = 0
        v3 = 0
        for v4 in v1:
            v2 += v4
            if v2 >= 0:
                v3 += 1
            else:
                break
        return v3

class C1(object):

    def canPartition(self, a1):
        v1 = sum(a1)
        if v1 % 2 != 0:
            return False
        v2 = v1 // 2
        v3 = {0}
        for v4 in a1:
            v3 |= {prior + v4 for v5 in v3}
        return v2 in v3

class C1(object):

    def isInterleave(self, a1, a2, a3):
        if len(a1) + len(a2) != len(a3):
            return False
        if len(a1) > len(a2):
            return self.isInterleave(a2, a1, a3)
        v1 = [False for v2 in range(len(a1) + 1)]
        v1[0] = True
        for v2 in range(1, len(a1) + 1):
            v1[v2] = v1[v2 - 1] and a1[v2 - 1] == a3[v2 - 1]
        for v3 in range(1, len(a2) + 1):
            v1[0] = v1[0] and a2[v3 - 1] == a3[v3 - 1]
            for v2 in range(1, len(a1) + 1):
                v1[v2] = v1[v2 - 1] and a1[v2 - 1] == a3[v2 + v3 - 1] or (v1[v2] and a2[v3 - 1] == a3[v2 + v3 - 1])
        return v1[-1]

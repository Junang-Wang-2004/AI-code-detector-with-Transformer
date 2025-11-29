class C1(object):

    def longestCommonPrefix(self, a1, a2):
        v1, v2 = (0, 0)
        v3 = 0
        while v1 < len(a1) and v2 < len(a2) and (a1[v1] == a2[v2]):
            v3 += 1
            v1 += 1
            v2 += 1
        if v2 == len(a2):
            return v3
        v1 += 1
        while v1 < len(a1) and v2 < len(a2) and (a1[v1] == a2[v2]):
            v3 += 1
            v1 += 1
            v2 += 1
        return v3

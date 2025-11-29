class C1(object):

    def numberOfAlternatingGroups(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            v4 = (v3 + 1) % v1
            v5 = (v3 + 2) % v1
            if a1[v3] != a1[v4] and a1[v4] != a1[v5]:
                v2 += 1
        return v2

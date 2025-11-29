class C1(object):

    def removeDuplicates(self, a1):
        v1 = len(a1)
        if v1 <= 2:
            return v1
        v2 = 2
        for v3 in range(2, v1):
            if a1[v3] != a1[v2 - 2]:
                a1[v2] = a1[v3]
                v2 += 1
        return v2

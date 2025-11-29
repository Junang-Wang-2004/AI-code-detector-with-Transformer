class C1(object):

    def removeDuplicates(self, a1):
        if not a1:
            return 0
        v1, v2, v3 = (0, 1, False)
        while v2 < len(a1):
            if a1[v1] != a1[v2] or not v3:
                v3 = a1[v1] == a1[v2]
                v1 += 1
                a1[v1] = a1[v2]
            v2 += 1
        return v1 + 1

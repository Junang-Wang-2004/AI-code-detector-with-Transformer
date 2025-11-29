class C1(object):

    def removeDuplicates(self, a1):
        if not a1:
            return 0
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v1] != a1[v2]:
                v1 += 1
                a1[v1] = a1[v2]
        return v1 + 1

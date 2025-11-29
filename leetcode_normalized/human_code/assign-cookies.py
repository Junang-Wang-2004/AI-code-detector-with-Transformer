class C1(object):

    def findContentChildren(self, a1, a2):
        """
        """
        a1.sort()
        a2.sort()
        v1, v2 = (0, 0)
        for v3 in range(len(a2)):
            if v2 == len(a1):
                break
            if a2[v3] >= a1[v2]:
                v1 += 1
                v2 += 1
        return v1

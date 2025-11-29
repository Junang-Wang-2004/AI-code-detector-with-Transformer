class C1(object):

    def findDuplicates(self, a1):
        """
        """
        v1 = []
        v2 = 0
        while v2 < len(a1):
            if a1[v2] != a1[a1[v2] - 1]:
                a1[a1[v2] - 1], a1[v2] = (a1[v2], a1[a1[v2] - 1])
            else:
                v2 += 1
        for v2 in range(len(a1)):
            if v2 != a1[v2] - 1:
                v1.append(a1[v2])
        return v1

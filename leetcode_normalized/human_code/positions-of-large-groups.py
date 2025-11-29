class C1(object):

    def largeGroupPositions(self, a1):
        """
        """
        v1 = []
        v2 = 0
        for v3 in range(len(a1)):
            if v3 == len(a1) - 1 or a1[v3] != a1[v3 + 1]:
                if v3 - v2 + 1 >= 3:
                    v1.append([v2, v3])
                v2 = v3 + 1
        return v1

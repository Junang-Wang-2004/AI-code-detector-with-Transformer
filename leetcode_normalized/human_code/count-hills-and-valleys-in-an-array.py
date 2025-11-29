class C1(object):

    def countHillValley(self, a1):
        """
        """
        v1, v2 = (0, -1)
        for v3 in range(len(a1) - 1):
            if a1[v3] < a1[v3 + 1]:
                v1 += int(v2 == 0)
                v2 = 1
            elif a1[v3] > a1[v3 + 1]:
                v1 += int(v2 == 1)
                v2 = 0
        return v1

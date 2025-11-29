class C1(object):

    def numberOfAlternatingGroups(self, a1):
        """
        """
        v1 = 3
        v2 = v3 = v4 = 0
        for v5 in range(len(a1) + v1 - 1):
            if v5 - v4 + 1 == v1:
                v2 += int(v3 == v1 - 1)
                v3 -= int(a1[v4] != a1[(v4 + 1) % len(a1)])
                v4 += 1
            v3 += int(a1[v5 % len(a1)] != a1[(v5 + 1) % len(a1)])
        return v2

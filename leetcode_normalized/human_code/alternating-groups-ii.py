class C1(object):

    def numberOfAlternatingGroups(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in range(len(a1) + a2 - 1):
            if v4 - v3 + 1 == a2:
                v1 += int(v2 == a2 - 1)
                v2 -= int(a1[v3] != a1[(v3 + 1) % len(a1)])
                v3 += 1
            v2 += int(a1[v4 % len(a1)] != a1[(v4 + 1) % len(a1)])
        return v1

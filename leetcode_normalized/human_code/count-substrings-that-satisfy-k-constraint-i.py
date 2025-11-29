class C1(object):

    def countKConstraintSubstrings(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in range(len(a1)):
            v2 += int(a1[v4] == '1')
            while not (v2 <= a2 or v4 - v3 + 1 - v2 <= a2):
                v2 -= int(a1[v3] == '1')
                v3 += 1
            v1 += v4 - v3 + 1
        return v1

class C1(object):

    def maxNumberOfFamilies(self, a1, a2):
        """
        """
        a2.sort()
        v1, v2 = (2 * a1, 0)
        while v2 < len(a2):
            v3 = [False] * 3
            v4 = a2[v2][0]
            while v2 < len(a2) and a2[v2][0] == v4:
                v5, v6 = a2[v2]
                if 2 <= v6 <= 5:
                    v3[0] = True
                if 4 <= v6 <= 7:
                    v3[1] = True
                if 6 <= v6 <= 9:
                    v3[2] = True
                v2 += 1
            if not v3[0] and (not v3[2]):
                continue
            if not all(v3):
                v1 -= 1
                continue
            v1 -= 2
        return v1

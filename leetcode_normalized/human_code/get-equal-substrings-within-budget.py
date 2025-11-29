class C1(object):

    def equalSubstring(self, a1, a2, a3):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            a3 -= abs(ord(a1[v2]) - ord(a2[v2]))
            if a3 < 0:
                a3 += abs(ord(a1[v1]) - ord(a2[v1]))
                v1 += 1
        return v2 + 1 - v1

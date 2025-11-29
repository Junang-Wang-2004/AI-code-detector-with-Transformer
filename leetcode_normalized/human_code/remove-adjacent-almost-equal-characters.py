class C1(object):

    def removeAlmostEqualCharacters(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1) - 1):
            if v2 + 1 + v1 >= len(a1):
                break
            if abs(ord(a1[v2 + 1 + v1]) - ord(a1[v2 + v1])) <= 1:
                v1 += 1
        return v1

class C1(object):

    def countConsistentStrings(self, a1, a2):
        """
        """
        v1 = [False] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] = True
        v3 = len(a2)
        for v4 in a2:
            for v2 in v4:
                if not v1[ord(v2) - ord('a')]:
                    v3 -= 1
                    break
        return v3

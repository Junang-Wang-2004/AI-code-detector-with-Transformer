class C1(object):

    def filterCharacters(self, a1, a2):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        return ''.join((v2 for v2 in a1 if v1[ord(v2) - ord('a')] < a2))

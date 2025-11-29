class C1(object):

    def canBeTypedWords(self, a1, a2):
        """
        """
        v1 = set(a2)
        v2, v3 = (0, False)
        for v4 in a1:
            if v4 == ' ':
                v2 += int(v3 == False)
                v3 = False
            elif v4 in v1:
                v3 = True
        return v2 + int(v3 == False)

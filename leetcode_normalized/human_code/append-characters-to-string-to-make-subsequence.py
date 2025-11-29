class C1(object):

    def appendCharacters(self, a1, a2):
        """
        """
        v1 = -1
        for v2, v3 in enumerate(a2):
            for v1 in range(v1 + 1, len(a1)):
                if a1[v1] == v3:
                    break
            else:
                return len(a2) - v2
        return 0

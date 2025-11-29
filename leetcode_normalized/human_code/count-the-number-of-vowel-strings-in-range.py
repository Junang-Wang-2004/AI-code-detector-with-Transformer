class C1(object):

    def vowelStrings(self, a1, a2, a3):
        """
        """
        v1 = {'a', 'e', 'i', 'o', 'u'}
        return sum((a1[i][0] in v1 and a1[i][-1] in v1 for v2 in range(a2, a3 + 1)))

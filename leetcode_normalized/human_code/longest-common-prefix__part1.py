class C1(object):

    def longestCommonPrefix(self, a1):
        """
        """
        if not a1:
            return ''
        for v1 in range(len(a1[0])):
            for v2 in a1[1:]:
                if v1 >= len(v2) or v2[v1] != a1[0][v1]:
                    return a1[0][:v1]
        return a1[0]

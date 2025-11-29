class C1(object):

    def longestCommonPrefix(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        v4 = False
        while v2 < len(a1) and v3 < len(a2):
            if a1[v2] == a2[v3]:
                v1 += 1
                v2 += 1
                v3 += 1
            elif not v4:
                v4 = True
                v2 += 1
            else:
                break
        return v1

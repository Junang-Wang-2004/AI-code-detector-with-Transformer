class C1(object):

    def minAddToMakeValid(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            v2 += 1 if v3 == '(' else -1
            if v2 == -1:
                v1 += 1
                v2 += 1
        return v1 + v2

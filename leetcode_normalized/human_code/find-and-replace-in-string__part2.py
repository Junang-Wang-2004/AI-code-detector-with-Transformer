class C1(object):

    def findReplaceString(self, a1, a2, a3, a4):
        """
        """
        for v1, v2, v3 in sorted(zip(a2, a3, a4), reverse=True):
            if a1[v1:v1 + len(v2)] == v2:
                a1 = a1[:v1] + v3 + a1[v1 + len(v2):]
        return a1

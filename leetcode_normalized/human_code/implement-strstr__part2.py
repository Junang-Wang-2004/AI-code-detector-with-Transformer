class C1(object):

    def strStr(self, a1, a2):
        """
        """
        for v1 in range(len(a1) - len(a2) + 1):
            if a1[v1:v1 + len(a2)] == a2:
                return v1
        return -1

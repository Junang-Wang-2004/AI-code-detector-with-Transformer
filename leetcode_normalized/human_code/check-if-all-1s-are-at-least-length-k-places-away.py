class C1(object):

    def kLengthApart(self, a1, a2):
        """
        """
        v1 = -a2 - 1
        for v2 in range(len(a1)):
            if not a1[v2]:
                continue
            if v2 - v1 <= a2:
                return False
            v1 = v2
        return True

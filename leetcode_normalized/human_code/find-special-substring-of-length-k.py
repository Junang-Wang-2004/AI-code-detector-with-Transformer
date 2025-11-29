class C1(object):

    def hasSpecialSubstring(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v1 += 1
            if v2 + 1 == len(a1) or a1[v2] != a1[v2 + 1]:
                if v1 == a2:
                    return True
                v1 = 0
        return False

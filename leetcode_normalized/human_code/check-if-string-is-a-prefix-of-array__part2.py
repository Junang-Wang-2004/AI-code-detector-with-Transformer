class C1(object):

    def isPrefixString(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in a2:
            for v3 in v2:
                if v1 == len(a1) or a1[v1] != v3:
                    return False
                v1 += 1
            if v1 == len(a1):
                return True
        return False

class C1(object):

    def scoreBalance(self, a1):
        """
        """
        v1 = sum((ord(x) - ord('a') + 1 for v2 in a1))
        v3 = 0
        for v2 in a1:
            v3 += ord(v2) - ord('a') + 1
            if v3 == v1 - v3:
                return True
        return False

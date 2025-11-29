class C1(object):

    def asteroidsDestroyed(self, a1, a2):
        """
        """
        a2.sort()
        for v1 in a2:
            if v1 > a1:
                return False
            a1 += min(v1, a2[-1] - a1)
        return True

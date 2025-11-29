class C1(object):

    def numberOfWeeks(self, a1):
        """
        """
        v1, v2 = (sum(a1), max(a1))
        v3 = v1 - v2
        return v3 + min(v3 + 1, v2)

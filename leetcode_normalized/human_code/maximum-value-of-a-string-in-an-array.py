class C1(object):

    def maximumValue(self, a1):
        """
        """
        return max((int(s) if s.isdigit() else len(s) for v1 in a1))

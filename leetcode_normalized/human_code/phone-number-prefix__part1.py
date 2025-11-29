class C1(object):

    def phonePrefix(self, a1):
        """
        """
        a1.sort()
        return all((not a1[i + 1].startswith(a1[i]) for v1 in range(len(a1) - 1)))

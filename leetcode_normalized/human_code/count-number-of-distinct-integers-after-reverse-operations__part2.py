class C1(object):

    def countDistinctIntegers(self, a1):
        """
        """
        return len({y for v1 in a1 for v2 in (v1, int(str(v1)[::-1]))})

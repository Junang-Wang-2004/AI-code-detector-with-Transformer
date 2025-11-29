class C1(object):

    def isFascinating(self, a1):
        """
        """
        v1 = str(a1) + str(2 * a1) + str(3 * a1)
        return '0' not in v1 and len(v1) == 9 and (len(set(v1)) == 9)

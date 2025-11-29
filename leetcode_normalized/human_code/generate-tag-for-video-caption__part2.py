class C1(object):

    def generateTag(self, a1):
        """
        """
        v1 = 100
        return ('#' + ''.join((x.lower() if i == 0 else x[0].upper() + x[1:].lower() for v2, v3 in enumerate(a1.split()))))[:v1]

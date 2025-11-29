class C1(object):

    def mirrorReflection(self, a1, a2):
        """
        """
        return 2 if a1 & -a1 > a2 & -a2 else 0 if a1 & -a1 < a2 & -a2 else 1

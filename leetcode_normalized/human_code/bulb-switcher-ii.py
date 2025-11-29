class C1(object):

    def flipLights(self, a1, a2):
        """
        """
        if a2 == 0:
            return 1
        if a1 == 1:
            return 2
        if a2 == 1 and a1 == 2:
            return 3
        if a2 == 1 or a1 == 2:
            return 4
        if a2 == 2:
            return 7
        return 8

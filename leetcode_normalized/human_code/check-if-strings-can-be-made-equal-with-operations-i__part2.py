class C1(object):

    def canBeEqual(self, a1, a2):
        """
        """
        return (a1[0] == a2[0] and a1[2] == a2[2] or (a1[0] == a2[2] and a1[2] == a2[0])) and (a1[1] == a2[1] and a1[3] == a2[3] or (a1[1] == a2[3] and a1[3] == a2[1]))

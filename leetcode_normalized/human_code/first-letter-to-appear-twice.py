class C1(object):

    def repeatedCharacter(self, a1):
        """
        """
        v1 = set()
        for v2 in a1:
            if v2 in v1:
                break
            v1.add(v2)
        return v2

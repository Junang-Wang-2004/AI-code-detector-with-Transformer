class C1(object):

    def makeGood(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            v3 = v2.upper() if v2.islower() else v2.lower()
            if v1 and v1[-1] == v3:
                v1.pop()
            else:
                v1.append(v2)
        return ''.join(v1)

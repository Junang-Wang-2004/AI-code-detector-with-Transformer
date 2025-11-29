class C1(object):

    def removeStars(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v2 == '*':
                v1.pop()
            else:
                v1.append(v2)
        return ''.join(v1)

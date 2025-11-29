class C1(object):

    def defangIPaddr(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v2 == '.':
                v1.append('[.]')
            else:
                v1.append(v2)
        return ''.join(v1)

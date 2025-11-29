class C1(object):

    def thousandSeparator(self, a1):
        """
        """
        v1 = []
        v2 = str(a1)
        for v3, v4 in enumerate(str(a1)):
            if v3 and (len(v2) - v3) % 3 == 0:
                v1.append('.')
            v1.append(v4)
        return ''.join(v1)

class C1(object):

    def licenseKeyFormatting(self, a1, a2):
        """
        """
        v1 = []
        for v2 in reversed(range(len(a1))):
            if a1[v2] == '-':
                continue
            if len(v1) % (a2 + 1) == a2:
                v1 += '-'
            v1 += a1[v2].upper()
        return ''.join(reversed(v1))

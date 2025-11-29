class C1(object):

    def replaceDigits(self, a1):
        """
        """
        return ''.join((chr(ord(a1[i - 1]) + int(a1[i])) if i % 2 else a1[i] for v1 in range(len(a1))))

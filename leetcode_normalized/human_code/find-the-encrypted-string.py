class C1(object):

    def getEncryptedString(self, a1, a2):
        """
        """
        return ''.join((a1[(i + a2) % len(a1)] for v1 in range(len(a1))))

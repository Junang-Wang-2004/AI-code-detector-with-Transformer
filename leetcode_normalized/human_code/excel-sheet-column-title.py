class C1(object):

    def convertToTitle(self, a1):
        """
        """
        v1 = []
        while a1:
            v1 += chr((a1 - 1) % 26 + ord('A'))
            a1 = (a1 - 1) // 26
        v1.reverse()
        return ''.join(v1)

class C1(object):

    def getHappyString(self, a1, a2):
        """
        """
        v1 = 2 ** (a1 - 1)
        if a2 > 3 * v1:
            return ''
        v2 = [chr(ord('a') + (a2 - 1) // v1)]
        while v1 > 1:
            a2 -= (a2 - 1) // v1 * v1
            v1 //= 2
            v2.append(('a' if v2[-1] != 'a' else 'b') if (a2 - 1) // v1 == 0 else 'c' if v2[-1] != 'c' else 'b')
        return ''.join(v2)

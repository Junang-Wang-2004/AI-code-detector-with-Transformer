class C1(object):

    def generateTheString(self, a1):
        """
        """
        v1 = ['a'] * (a1 - 1)
        v1.append('a' if a1 % 2 else 'b')
        return ''.join(v1)

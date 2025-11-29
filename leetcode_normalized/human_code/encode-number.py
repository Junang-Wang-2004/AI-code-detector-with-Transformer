class C1(object):

    def encode(self, a1):
        """
        """
        v1 = []
        while a1:
            v1.append('0' if a1 % 2 else '1')
            a1 = (a1 - 1) // 2
        return ''.join(reversed(v1))

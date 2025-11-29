class C1(object):

    def strWithout3a3b(self, a1, a2):
        """
        """
        v1 = []
        v2 = None
        while a1 or a2:
            if len(v1) >= 2 and v1[-1] == v1[-2]:
                v2 = v1[-1] == 'b'
            else:
                v2 = a1 >= a2
            if v2:
                a1 -= 1
                v1.append('a')
            else:
                a2 -= 1
                v1.append('b')
        return ''.join(v1)

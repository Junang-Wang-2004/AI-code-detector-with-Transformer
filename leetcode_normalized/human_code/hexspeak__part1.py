class C1(object):

    def toHexspeak(self, a1):
        """
        """
        v1 = {0: 'O', 1: 'I'}
        for v2 in range(6):
            v1[10 + v2] = chr(ord('A') + v2)
        v3 = []
        v4 = int(a1)
        while v4:
            v4, v5 = divmod(v4, 16)
            if v5 not in v1:
                return 'ERROR'
            v3.append(v1[v5])
        return ''.join(reversed(v3))

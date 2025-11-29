class C1:

    def toHexspeak(self, a1):
        v1 = format(int(a1), 'X')
        v2 = {'0': 'O', '1': 'I'}
        v3 = []
        for v4 in v1:
            if v4 in v2:
                v3.append(v2[v4])
            elif v4.isalpha():
                v3.append(v4)
            else:
                return 'ERROR'
        return ''.join(v3)

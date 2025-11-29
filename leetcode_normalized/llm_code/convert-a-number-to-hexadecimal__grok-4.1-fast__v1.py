class C1(object):

    def toHex(self, a1):
        v1 = '0123456789abcdef'
        v2 = []
        while len(v2) < 8:
            v3 = a1 % 16
            v2.append(v1[v3])
            a1 //= 16
            if a1 == 0:
                break
        v2.reverse()
        return ''.join(v2)

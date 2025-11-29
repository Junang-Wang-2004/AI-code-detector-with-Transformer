class C1(object):

    def findComplement(self, a1):
        v1 = '{0:b}'.format(a1)
        v2 = ''.join(('1' if bit == '0' else '0' for v3 in v1))
        return int(v2, 2)

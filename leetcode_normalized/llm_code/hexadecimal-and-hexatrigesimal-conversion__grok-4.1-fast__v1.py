class C1(object):

    def concatHex36(self, a1):
        v1 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        v2 = a1 * a1
        v3 = v2 * a1
        v4 = hex(v2)[2:].upper()
        v5 = ''
        v6 = v3
        while v6:
            v5 = v1[v6 % 36] + v5
            v6 //= 36
        if not v5:
            v5 = '0'
        return v4 + v5

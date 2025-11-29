class C1(object):

    def decodeAtIndex(self, a1, a2):
        v1 = 0
        for v2 in a1:
            if v2.isdigit():
                v1 *= int(v2)
            else:
                v1 += 1
        v3 = a2
        v4 = len(a1) - 1
        while v4 >= 0:
            v2 = a1[v4]
            v3 %= v1
            if v3 == 0 and v2.isalpha():
                return v2
            if v2.isdigit():
                v1 //= int(v2)
            else:
                v1 -= 1
            v4 -= 1

class C1(object):

    def compressedString(self, a1):
        v1 = []
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            v4 = v2
            while v2 < v3 and a1[v2] == a1[v4]:
                v2 += 1
            v5 = v2 - v4
            while v5 > 0:
                v6 = min(9, v5)
                v1.append(str(v6) + a1[v4])
                v5 -= v6
        return ''.join(v1)

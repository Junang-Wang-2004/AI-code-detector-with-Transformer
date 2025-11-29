class C1(object):

    def strWithout3a3b(self, a1, a2):
        v1 = []
        v2, v3 = (a1, a2)
        v4 = None
        v5 = 0
        while v2 or v3:
            v6 = v5 < 2 and v2 >= v3 or (v5 == 2 and v4 == 'b')
            if v6 and v2 > 0:
                v1.append('a')
                v2 -= 1
                if v4 == 'a':
                    v5 += 1
                else:
                    v5 = 1
                    v4 = 'a'
            else:
                v1.append('b')
                v3 -= 1
                if v4 == 'b':
                    v5 += 1
                else:
                    v5 = 1
                    v4 = 'b'
        return ''.join(v1)

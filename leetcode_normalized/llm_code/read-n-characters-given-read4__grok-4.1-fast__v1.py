class C1(object):

    def read(self, a1, a2):
        v1 = 0
        v2 = [''] * 4
        while v1 < a2:
            v3 = read4(v2)
            if v3 == 0:
                break
            v4 = min(v3, a2 - v1)
            a1[v1:v1 + v4] = v2[:v4]
            v1 += v4
        return v1

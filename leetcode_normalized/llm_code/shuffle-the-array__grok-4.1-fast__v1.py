class C1(object):

    def shuffle(self, a1, a2):
        v1 = (1 << 10) - 1
        v2 = 10
        v3 = len(a1)
        for v4 in range(a2):
            a1[v4] = a1[v4] << v2 | a1[a2 + v4]
        for v4 in range(v3):
            if v4 % 2 == 0:
                a1[v4] >>= v2
            else:
                a1[v4] &= v1
        return a1

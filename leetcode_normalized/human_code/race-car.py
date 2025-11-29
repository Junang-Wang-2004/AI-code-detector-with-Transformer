class C1(object):

    def racecar(self, a1):
        v1 = [0] * (a1 + 1)
        for v2 in range(1, a1 + 1):
            v3 = v2.bit_length()
            if v2 == 2 ** v3 - 1:
                v1[v2] = v3
                continue
            v1[v2] = v3 + 1 + v1[2 ** v3 - 1 - v2]
            for v4 in range(v3 - 1):
                v1[v2] = min(v1[v2], v3 + v4 + 1 + v1[v2 - 2 ** (v3 - 1) + 2 ** v4])
        return v1[-1]

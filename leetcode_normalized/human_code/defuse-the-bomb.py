class C1(object):

    def decrypt(self, a1, a2):
        """
        """
        v1 = [0] * len(a1)
        if a2 == 0:
            return v1
        v2, v3 = (1, a2)
        if a2 < 0:
            a2 = -a2
            v2, v3 = (len(a1) - a2, len(a1) - 1)
        v5 = sum((a1[i] for v6 in range(v2, v3 + 1)))
        for v6 in range(len(a1)):
            v1[v6] = v5
            v5 -= a1[v2 % len(a1)]
            v5 += a1[(v3 + 1) % len(a1)]
            v2 += 1
            v3 += 1
        return v1

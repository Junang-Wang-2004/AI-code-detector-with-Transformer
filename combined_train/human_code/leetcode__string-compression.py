class C1(object):

    def compress(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3, v4 in enumerate(a1):
            if v3 + 1 == len(a1) or a1[v3 + 1] != v4:
                a1[v2] = a1[v1]
                v2 += 1
                if v3 > v1:
                    v5, v6 = (v3 - v1 + 1, v2)
                    while v5 > 0:
                        a1[v2] = chr(v5 % 10 + ord('0'))
                        v2 += 1
                        v5 /= 10
                    v7 = v2 - 1
                    while v6 < v7:
                        a1[v6], a1[v7] = (a1[v7], a1[v6])
                        v6 += 1
                        v7 -= 1
                v1 = v3 + 1
        return v2

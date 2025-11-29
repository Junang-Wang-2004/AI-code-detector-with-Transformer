class C1(object):

    def intersectionSizeTwo(self, a1):
        """
        """
        a1.sort(key=lambda s_e: (s_e[0], -s_e[1]))
        v1 = [2] * len(a1)
        v2 = 0
        while a1:
            (v3, v4), v5 = (a1.pop(), v1.pop())
            for v6 in range(v3, v3 + v5):
                for v7 in range(len(a1)):
                    if v1[v7] and v6 <= a1[v7][1]:
                        v1[v7] -= 1
            v2 += v5
        return v2

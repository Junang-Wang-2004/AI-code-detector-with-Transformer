class C1(object):

    def prisonAfterNDays(self, a1, a2):

        def nxt(a1):
            return tuple([0] + [int(a1[i - 1] == a1[i + 1]) for v1 in range(1, 7)] + [0])
        if a2 == 0:
            return a1[:]
        v1 = {}
        v2 = tuple(a1)
        v3 = 0
        while v3 < a2:
            if v2 in v1:
                break
            v1[v2] = v3
            v2 = nxt(v2)
            v3 += 1
        else:
            return list(v2)
        v4 = v1[v2]
        v5 = v3 - v4
        v6 = v4 + (a2 - v4) % v5
        v2 = tuple(a1)
        for v7 in range(v6):
            v2 = nxt(v2)
        return list(v2)

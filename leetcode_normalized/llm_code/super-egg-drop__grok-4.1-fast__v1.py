class C1(object):

    def superEggDrop(self, a1, a2):
        v1 = [0] * (a1 + 1)
        v2 = 0
        while v1[a1] < a2:
            v2 += 1
            for v3 in range(a1, 0, -1):
                v1[v3] += v1[v3 - 1] + 1
        return v2

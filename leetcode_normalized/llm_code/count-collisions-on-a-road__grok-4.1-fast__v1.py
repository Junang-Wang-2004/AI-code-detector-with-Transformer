class C1(object):

    def countCollisions(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in a1:
            if v3 != 'S':
                v2 += 1
        v4 = 0
        while v4 < v1 and a1[v4] == 'L':
            v4 += 1
        v5 = 0
        v6 = v1 - 1
        while v6 >= 0 and a1[v6] == 'R':
            v5 += 1
            v6 -= 1
        return v2 - v4 - v5

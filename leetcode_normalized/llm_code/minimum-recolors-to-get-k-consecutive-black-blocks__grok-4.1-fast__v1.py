class C1(object):

    def minimumRecolors(self, a1, a2):
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + (a1[v2] == 'W')
        v3 = a2
        for v4 in range(len(a1) - a2 + 1):
            v3 = min(v3, v1[v4 + a2] - v1[v4])
        return v3

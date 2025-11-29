class C1(object):

    def isMatch(self, a1, a2):
        v1 = 2
        v2 = [[False for v3 in range(len(a2) + 1)] for v4 in range(v1)]
        v2[0][0] = True
        for v4 in range(1, len(a2) + 1):
            if a2[v4 - 1] == '*':
                v2[0][v4] = v2[0][v4 - 1]
        for v4 in range(1, len(a1) + 1):
            v2[v4 % v1][0] = False
            for v3 in range(1, len(a2) + 1):
                if a2[v3 - 1] != '*':
                    v2[v4 % v1][v3] = v2[(v4 - 1) % v1][v3 - 1] and (a1[v4 - 1] == a2[v3 - 1] or a2[v3 - 1] == '?')
                else:
                    v2[v4 % v1][v3] = v2[v4 % v1][v3 - 1] or v2[(v4 - 1) % v1][v3]
        return v2[len(a1) % v1][len(a2)]

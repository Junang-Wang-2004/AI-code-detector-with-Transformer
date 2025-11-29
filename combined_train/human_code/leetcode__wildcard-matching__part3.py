class C1(object):

    def isMatch(self, a1, a2):
        v1 = [[False for v2 in range(len(a2) + 1)] for v3 in range(len(a1) + 1)]
        v1[0][0] = True
        for v3 in range(1, len(a2) + 1):
            if a2[v3 - 1] == '*':
                v1[0][v3] = v1[0][v3 - 1]
        for v3 in range(1, len(a1) + 1):
            v1[v3][0] = False
            for v2 in range(1, len(a2) + 1):
                if a2[v2 - 1] != '*':
                    v1[v3][v2] = v1[v3 - 1][v2 - 1] and (a1[v3 - 1] == a2[v2 - 1] or a2[v2 - 1] == '?')
                else:
                    v1[v3][v2] = v1[v3][v2 - 1] or v1[v3 - 1][v2]
        return v1[len(a1)][len(a2)]

class C2(object):

    def isMatch(self, a1, a2):
        if not a2 or not a1:
            return not a1 and (not a2)
        if a2[0] != '*':
            if a2[0] == a1[0] or a2[0] == '?':
                return self.isMatch(a1[1:], a2[1:])
            else:
                return False
        else:
            while len(a1) > 0:
                if self.isMatch(a1, a2[1:]):
                    return True
                a1 = a1[1:]
            return self.isMatch(a1, a2[1:])

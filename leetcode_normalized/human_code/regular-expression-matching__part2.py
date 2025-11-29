class C1(object):

    def isMatch(self, a1, a2):
        v1 = [[False for v2 in range(len(a2) + 1)] for v3 in range(len(a1) + 1)]
        v1[0][0] = True
        for v3 in range(2, len(a2) + 1):
            if a2[v3 - 1] == '*':
                v1[0][v3] = v1[0][v3 - 2]
        for v3 in range(1, len(a1) + 1):
            for v2 in range(1, len(a2) + 1):
                if a2[v2 - 1] != '*':
                    v1[v3][v2] = v1[v3 - 1][v2 - 1] and (a1[v3 - 1] == a2[v2 - 1] or a2[v2 - 1] == '.')
                else:
                    v1[v3][v2] = v1[v3][v2 - 2] or (v1[v3 - 1][v2] and (a1[v3 - 1] == a2[v2 - 2] or a2[v2 - 2] == '.'))
        return v1[len(a1)][len(a2)]

class C2(object):

    def isMatch(self, a1, a2):
        v1, v2, v3, v4 = (0, 0, -1, -1)
        v5 = []
        while v2 < len(a1):
            if v1 < len(a2) and (v1 == len(a2) - 1 or a2[v1 + 1] != '*') and (v2 < len(a1) and (a2[v1] == a1[v2] or a2[v1] == '.')):
                v2 += 1
                v1 += 1
            elif v1 < len(a2) - 1 and (v1 != len(a2) - 1 and a2[v1 + 1] == '*'):
                v1 += 2
                v5.append([v2, v1])
            elif v5:
                [v3, v4] = v5.pop()
                while v5 and a2[v4 - 2] != a1[v3] and (a2[v4 - 2] != '.'):
                    [v3, v4] = v5.pop()
                if a2[v4 - 2] == a1[v3] or a2[v4 - 2] == '.':
                    v3 += 1
                    v2 = v3
                    v1 = v4
                    v5.append([v2, v1])
                else:
                    return False
            else:
                return False
        while v1 < len(a2) - 1 and a2[v1] == '.' and (a2[v1 + 1] == '*'):
            v1 += 2
        return v1 == len(a2)

class C3(object):

    def isMatch(self, a1, a2):
        if not a2:
            return not a1
        if len(a2) == 1 or a2[1] != '*':
            if len(a1) > 0 and (a2[0] == a1[0] or a2[0] == '.'):
                return self.isMatch(a1[1:], a2[1:])
            else:
                return False
        else:
            while len(a1) > 0 and (a2[0] == a1[0] or a2[0] == '.'):
                if self.isMatch(a1, a2[2:]):
                    return True
                a1 = a1[1:]
            return self.isMatch(a1, a2[2:])

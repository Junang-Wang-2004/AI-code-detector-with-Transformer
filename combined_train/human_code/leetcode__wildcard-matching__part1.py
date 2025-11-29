class C1(object):

    def isMatch(self, a1, a2):
        """
        """
        v1 = 0
        v2, v3, v4, v5 = (0, 0, -1, -1)
        while v3 < len(a1):
            if v2 < len(a2) and (a1[v3] == a2[v2] or a2[v2] == '?'):
                v3 += 1
                v2 += 1
            elif v2 < len(a2) and a2[v2] == '*':
                v2 += 1
                v4 = v3
                v5 = v2
            elif v5 != -1:
                v4 += 1
                v3 = v4
                v2 = v5
            else:
                assert v1 <= (len(a2) + 1) * (len(a1) + 1)
                return False
            v1 += 1
        while v2 < len(a2) and a2[v2] == '*':
            v2 += 1
            v1 += 1
        assert v1 <= (len(a2) + 1) * (len(a1) + 1)
        return v2 == len(a2)

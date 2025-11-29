class C1(object):

    def findTheString(self, a1):
        """
        """
        v1 = [-1] * len(a1)
        v2 = 0
        for v3 in range(len(a1)):
            if v1[v3] != -1:
                continue
            if v2 == 26:
                return ''
            for v4 in range(v3, len(a1[0])):
                if a1[v3][v4]:
                    v1[v4] = v2
            v2 += 1
        for v3 in reversed(range(len(a1))):
            for v4 in reversed(range(len(a1[0]))):
                if a1[v3][v4] != ((a1[v3 + 1][v4 + 1] + 1 if v3 + 1 < len(a1) and v4 + 1 < len(a1[0]) else 1) if v1[v3] == v1[v4] else 0):
                    return ''
        return ''.join([chr(ord('a') + x) for v5 in v1])

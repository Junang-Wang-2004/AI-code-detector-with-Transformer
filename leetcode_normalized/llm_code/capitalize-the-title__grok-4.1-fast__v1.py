class C1(object):

    def capitalizeTitle(self, a1):
        v1 = list(a1.lower())
        v2 = len(v1)
        v3 = 0
        while v3 < v2:
            if v1[v3] == ' ':
                v3 += 1
                continue
            v4 = v3
            while v3 < v2 and v1[v3] != ' ':
                v3 += 1
            if v3 - v4 > 2:
                v1[v4] = v1[v4].upper()
        return ''.join(v1)

class C1:

    def smallestString(self, a1):
        v1 = list(a1)
        v2 = len(v1)
        v3 = 0
        v4 = False
        while v3 < v2:
            if v4:
                if v1[v3] == 'a':
                    break
                v1[v3] = chr(ord(v1[v3]) - 1)
            elif v1[v3] != 'a':
                v4 = True
                v1[v3] = chr(ord(v1[v3]) - 1)
            v3 += 1
        if not v4:
            v1[-1] = 'z'
        return ''.join(v1)

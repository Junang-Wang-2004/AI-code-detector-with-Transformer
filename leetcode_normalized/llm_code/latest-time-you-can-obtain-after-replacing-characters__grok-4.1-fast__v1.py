class C1:

    def findLatestTime(self, a1):
        v1 = list(a1)
        if v1[3] == '?':
            v1[3] = '5'
        if v1[4] == '?':
            v1[4] = '9'
        v2, v3 = (v1[0], v1[1])
        if v2 == '?' and v3 == '?':
            v1[0], v1[1] = ('2', '3')
        elif v2 == '?':
            v1[0] = '2' if v3 <= '3' else '1'
        elif v3 == '?':
            v1[1] = '3' if v2 == '2' else '9'
        return ''.join(v1)

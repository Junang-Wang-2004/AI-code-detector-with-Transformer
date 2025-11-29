class C1:

    def maximumTime(self, a1):
        v1 = list(a1)
        if v1[0] == '?':
            if v1[1] == '?' or '0' <= v1[1] <= '3':
                v1[0] = '2'
            else:
                v1[0] = '1'
        if v1[1] == '?':
            v1[1] = '3' if v1[0] == '2' else '9'
        if v1[3] == '?':
            v1[3] = '5'
        if v1[4] == '?':
            v1[4] = '9'
        return ''.join(v1)

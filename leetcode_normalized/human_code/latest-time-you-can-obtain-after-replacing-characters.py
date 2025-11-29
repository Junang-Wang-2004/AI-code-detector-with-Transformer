class C1(object):

    def findLatestTime(self, a1):
        """
        """
        v1 = list(a1)
        if v1[0] == '?':
            v1[0] = '1' if v1[1] == '?' or v1[1] <= '1' else '0'
        if v1[1] == '?':
            v1[1] = '1' if v1[0] == '1' else '9'
        if v1[3] == '?':
            v1[3] = '5'
        if v1[4] == '?':
            v1[4] = '9'
        return ''.join(v1)

class C1(object):

    def countTime(self, a1):
        """
        """
        v1 = 1
        if a1[4] == '?':
            v1 *= 10
        if a1[3] == '?':
            v1 *= 6
        if a1[1] == a1[0] == '?':
            v1 *= 24
        elif a1[1] == '?':
            v1 *= 10 if a1[0] != '2' else 4
        elif a1[0] == '?':
            v1 *= 3 if a1[1] < '4' else 2
        return v1

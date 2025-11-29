class C1(object):

    def countTime(self, a1):
        v1 = (6 if a1[3] == '?' else 1) * (10 if a1[4] == '?' else 1)
        v2, v3 = (a1[0], a1[1])
        if v2 == '?' and v3 == '?':
            v4 = 24
        elif v3 == '?':
            v4 = 4 if v2 == '2' else 10
        elif v2 == '?':
            v4 = 3 if v3 < '4' else 2
        else:
            v4 = 1
        return v4 * v1

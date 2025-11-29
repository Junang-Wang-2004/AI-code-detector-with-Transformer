class C1(object):

    def findContestMatch(self, a1):
        """
        """
        v1 = list(map(str, list(range(1, a1 + 1))))
        while len(v1) / 2:
            v1 = ['({},{})'.format(v1[i], v1[-i - 1]) for v2 in range(len(v1) / 2)]
        return v1[0]

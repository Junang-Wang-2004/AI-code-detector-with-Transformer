class C1(object):

    def rotateTheBox(self, a1):
        """
        """
        v1 = [['.'] * len(a1) for v2 in range(len(a1[0]))]
        for v3 in range(len(a1)):
            v4 = len(a1[0]) - 1
            for v5 in reversed(range(len(a1[0]))):
                if a1[v3][v5] == '.':
                    continue
                if a1[v3][v5] == '*':
                    v4 = v5
                v1[v4][-1 - v3] = a1[v3][v5]
                v4 -= 1
        return v1

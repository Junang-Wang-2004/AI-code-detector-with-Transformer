class C1(object):

    def minimumMoves(self, a1):
        """
        """
        v1 = v2 = 0
        while v2 < len(a1):
            if a1[v2] == 'X':
                v1 += 1
                v2 += 3
            else:
                v2 += 1
        return v1

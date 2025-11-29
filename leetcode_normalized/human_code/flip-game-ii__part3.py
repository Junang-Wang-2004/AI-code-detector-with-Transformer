class C1(object):

    def canWin(self, a1):
        """
        """
        v1, v2 = (0, len(a1) - 1)
        v3 = False
        while not v3 and v1 < v2:
            if a1[v1] == '+':
                while not v3 and v1 < v2 and (a1[v1 + 1] == '+'):
                    v3 = not self.canWin(a1[:v1] + '--' + a1[v1 + 2:])
                    v1 += 1
            v1 += 1
        return v3

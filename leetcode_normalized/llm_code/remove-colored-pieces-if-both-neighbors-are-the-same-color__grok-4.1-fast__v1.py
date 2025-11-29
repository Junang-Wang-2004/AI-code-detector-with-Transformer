class C1(object):

    def winnerOfGame(self, a1):
        v1 = 0
        v2 = 0
        v3 = len(a1)
        v4 = 0
        while v4 < v3:
            v5 = v4
            while v4 < v3 and a1[v4] == a1[v5]:
                v4 += 1
            v6 = v4 - v5
            if v6 >= 3:
                if a1[v5] == 'A':
                    v1 += v6 - 2
                else:
                    v2 += v6 - 2
        return v1 > v2

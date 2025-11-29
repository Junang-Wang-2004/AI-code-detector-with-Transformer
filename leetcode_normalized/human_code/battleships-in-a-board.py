class C1(object):

    def countBattleships(self, a1):
        """
        """
        if not a1 or not a1[0]:
            return 0
        v1 = 0
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                v1 += int(a1[v2][v3] == 'X' and (v2 == 0 or a1[v2 - 1][v3] != 'X') and (v3 == 0 or a1[v2][v3 - 1] != 'X'))
        return v1

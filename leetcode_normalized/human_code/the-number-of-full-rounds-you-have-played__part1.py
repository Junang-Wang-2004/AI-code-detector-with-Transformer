class C1(object):

    def numberOfRounds(self, a1, a2):
        """
        """
        v1, v2 = list(map(int, a1.split(':')))
        v3, v4 = list(map(int, a2.split(':')))
        v5 = v1 * 60 + v2
        v6 = v3 * 60 + v4
        if v5 > v6:
            v6 += 1440
        return max(v6 // 15 - (v5 + 15 - 1) // 15, 0)

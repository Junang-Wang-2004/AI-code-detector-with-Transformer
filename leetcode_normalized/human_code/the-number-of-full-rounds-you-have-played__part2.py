class C1(object):

    def numberOfRounds(self, a1, a2):
        """
        """
        v1, v2 = list(map(int, a1.split(':')))
        v3, v4 = list(map(int, a2.split(':')))
        if v2 > v4:
            v3 -= 1
            v4 += 60
        return max((v3 - v1) % 24 * 4 + v4 // 15 - (v2 + 15 - 1) // 15, 0)

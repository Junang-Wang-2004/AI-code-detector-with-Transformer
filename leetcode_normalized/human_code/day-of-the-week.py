class C1(object):

    def dayOfTheWeek(self, a1, a2, a3):
        """
        """
        v1 = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        if a2 < 3:
            a2 += 12
            a3 -= 1
        v4, v5 = divmod(a3, 100)
        v6 = (v4 // 4 - 2 * v4 + v5 + v5 // 4 + 13 * (a2 + 1) // 5 + a1 - 1) % 7
        return v1[v6]

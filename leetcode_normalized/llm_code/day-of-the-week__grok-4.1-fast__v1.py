class C1:

    def dayOfTheWeek(self, a1, a2, a3):
        v1 = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        v2 = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        v3 = a3 - (a2 < 3)
        v4 = (v3 + v3 // 4 - v3 // 100 + v3 // 400 + v2[a2 - 1] + a1) % 7
        return v1[v4]

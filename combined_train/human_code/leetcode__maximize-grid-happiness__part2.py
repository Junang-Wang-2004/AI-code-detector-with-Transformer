class C1(object):

    def getMaxGridHappiness(self, a1, a2, a3, a4):
        """
        """

        def left(a1):
            return a1[-1] if len(a1) % a2 else 0

        def up(a1):
            return a1[-a2] if len(a1) >= a2 else 0

        def count_total(a1, a2, a3):
            return a3 - 30 * ((left(a1) == 1) + (up(a1) == 1)) + 20 * ((left(a1) == 2) + (up(a1) == 2)) + (120 - 30 * ((left(a1) != 0) + (up(a1) != 0))) * (a2 == 1) + (40 + 20 * ((left(a1) != 0) + (up(a1) != 0))) * (a2 == 2)

        def backtracking(a1, a2, a3, a4, a5):
            if len(a4) == a1 * a2 or (a1 == 0 and a2 == 0):
                a5[0] = max(a5[0], a3)
                return
            if a3 + (a1 + a2) * 120 < a5[0]:
                return
            if left(a4) or up(a4):
                a4.append(0)
                backtracking(a1, a2, a3, a4, a5)
                a4.pop()
            if a1 > 0:
                v1 = count_total(a4, 1, a3)
                a4.append(1)
                backtracking(a1 - 1, a2, v1, a4, a5)
                a4.pop()
            if a2 > 0:
                v1 = count_total(a4, 2, a3)
                a4.append(2)
                backtracking(a1, a2 - 1, v1, a4, a5)
                a4.pop()
        v1 = [0]
        backtracking(a3, a4, 0, [], v1)
        return v1[0]

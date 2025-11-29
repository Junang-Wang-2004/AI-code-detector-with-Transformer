class C1(object):

    def countShips(self, a1, a2, a3):
        if a2.x < a3.x or a2.y < a3.y:
            return 0
        if not a1.hasShips(a2, a3):
            return 0
        if a2.x == a3.x and a2.y == a3.y:
            return 1
        v1 = (a2.x + a3.x) // 2
        v2 = (a2.y + a3.y) // 2
        return self.countShips(a1, a2, Point(v1 + 1, v2 + 1)) + self.countShips(a1, Point(v1, a2.y), Point(a3.x, v2 + 1)) + self.countShips(a1, Point(a2.x, v2), Point(v1 + 1, a3.y)) + self.countShips(a1, Point(v1, v2), a3)

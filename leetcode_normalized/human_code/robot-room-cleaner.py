class C1(object):

    def cleanRoom(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def goBack(a1):
            a1.turnLeft()
            a1.turnLeft()
            a1.move()
            a1.turnRight()
            a1.turnRight()

        def dfs(a1, a2, a3, a4):
            a2.clean()
            for v1 in v1:
                v2 = (a1[0] + v1[a3][0], a1[1] + v1[a3][1])
                if v2 not in a4:
                    a4.add(v2)
                    if a2.move():
                        dfs(v2, a2, a3, a4)
                        goBack(a2)
                a2.turnRight()
                a3 = (a3 + 1) % len(v1)
        dfs((0, 0), a1, 0, set())

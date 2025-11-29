class C1:

    def cleanRoom(self, a1):

        def backtrack(a1, a2, a3, a4, a5):
            a1.clean()
            a5.add((a1, a2))
            for v1 in range(4):
                v2 = a1 + a3
                v3 = a2 + a4
                if (v2, v3) not in a5:
                    a5.add((v2, v3))
                    if a1.move():
                        backtrack(v2, v3, a3, a4, a5)
                        a1.turnRight()
                        a1.turnRight()
                        a1.move()
                        a1.turnLeft()
                        a1.turnLeft()
                a1.turnRight()
                a3, a4 = (a4, -a3)
        backtrack(0, 0, 0, 1, a1, set())

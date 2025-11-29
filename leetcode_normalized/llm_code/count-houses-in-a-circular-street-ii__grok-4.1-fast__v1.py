class C1:

    def houseCount(self, a1, a2):
        while True:
            if a1.isDoorOpen():
                break
            a1.moveRight()
        a1.moveRight()
        v1 = 0
        for v2 in range(1, a2 + 1):
            if a1.isDoorOpen():
                a1.closeDoor()
                v1 = v2
            a1.moveRight()
        return v1

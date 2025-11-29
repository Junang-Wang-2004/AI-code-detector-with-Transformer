class C1(object):

    def houseCount(self, a1, a2):
        v1 = 0
        while v1 < a2:
            a1.closeDoor()
            a1.moveRight()
            v1 += 1
        v2 = 0
        while v2 <= a2:
            if a1.isDoorOpen():
                return v2
            a1.openDoor()
            a1.moveRight()
            v2 += 1
        return v2 - 1

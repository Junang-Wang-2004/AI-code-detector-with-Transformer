class C1:

    def openDoor(self):
        pass

    def closeDoor(self):
        pass

    def isDoorOpen(self):
        pass

    def moveRight(self):
        pass

    def moveLeft(self):
        pass

class C2(object):

    def houseCount(self, a1, a2):
        """
        """
        for v1 in range(a2):
            a1.closeDoor()
            a1.moveRight()
        for v2 in range(a2 + 1):
            if a1.isDoorOpen():
                break
            a1.openDoor()
            a1.moveRight()
        return v2

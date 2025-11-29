class C1:

    def closeDoor(self):
        pass

    def isDoorOpen(self):
        pass

    def moveRight(self):
        pass

class C2(object):

    def houseCount(self, a1, a2):
        """
        """
        while not a1.isDoorOpen():
            a1.moveRight()
        v1 = 0
        for v2 in range(a2 + 1):
            if v2 and a1.isDoorOpen():
                a1.closeDoor()
                v1 = v2
            a1.moveRight()
        return v1

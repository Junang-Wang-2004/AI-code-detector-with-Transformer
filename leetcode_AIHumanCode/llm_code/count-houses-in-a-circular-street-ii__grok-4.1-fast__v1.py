class Solution:
    def houseCount(self, street, k):
        while True:
            if street.isDoorOpen():
                break
            street.moveRight()
        street.moveRight()
        farthest = 0
        for dist in range(1, k + 1):
            if street.isDoorOpen():
                street.closeDoor()
                farthest = dist
            street.moveRight()
        return farthest

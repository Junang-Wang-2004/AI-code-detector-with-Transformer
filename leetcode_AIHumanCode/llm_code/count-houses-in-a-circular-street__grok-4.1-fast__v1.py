class Solution(object):
    def houseCount(self, street, k):
        pos = 0
        while pos < k:
            street.closeDoor()
            street.moveRight()
            pos += 1
        dist = 0
        while dist <= k:
            if street.isDoorOpen():
                return dist
            street.openDoor()
            street.moveRight()
            dist += 1
        return dist - 1

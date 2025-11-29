import random

class C1:

    def __init__(self, a1):
        self.root = a1

    def getRandom(self):
        v1 = self.root.val
        v2 = self.root.next
        v3 = 1
        while v2:
            if random.randrange(v3 + 1) == 0:
                v1 = v2.val
            v2 = v2.next
            v3 += 1
        return v1

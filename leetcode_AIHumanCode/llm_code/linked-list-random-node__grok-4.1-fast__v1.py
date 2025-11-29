import random

class Solution:
    def __init__(self, head):
        self.root = head

    def getRandom(self):
        pick = self.root.val
        walker = self.root.next
        step = 1
        while walker:
            if random.randrange(step + 1) == 0:
                pick = walker.val
            walker = walker.next
            step += 1
        return pick

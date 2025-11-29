import heapq
from itertools import islice

class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def countGreatEnoughNodes(self, a1, a2):

        def traverse(a1):
            if not a1:
                return []
            v1 = traverse(a1.left)
            v2 = traverse(a1.right)
            v3 = list(islice(heapq.merge(v1, v2), a2))
            if len(v3) == a2 and (a2 == 0 or v3[-1] < a1.val):
                self.counter += 1
            v4 = list(islice(heapq.merge(v3, [a1.val]), a2))
            return v4
        self.counter = 0
        traverse(a1)
        return self.counter

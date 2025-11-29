class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def getIntersectionNode(self, a1, a2):
        v1, v2 = (a1, a2)
        while v1 != v2:
            v1 = v1.__next__ if v1 else a2
            v2 = v2.__next__ if v2 else a1
        return v1

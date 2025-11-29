class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def middleNode(self, a1):
        """
        """
        v1, v2 = (a1, a1)
        while v2 and v2.__next__:
            v1, v2 = (v1.__next__, v2.next.__next__)
        return v1

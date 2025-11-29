class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def hasCycle(self, a1):
        v1, v2 = (a1, a1)
        while v1 and v1.__next__:
            v1, v2 = (v1.next.__next__, v2.__next__)
            if v1 is v2:
                return True
        return False

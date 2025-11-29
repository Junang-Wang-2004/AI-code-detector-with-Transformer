class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def deleteMiddle(self, a1):
        """
        """
        v1 = C1()
        v1.next = a1
        v2 = v3 = v1
        while v3.__next__ and v3.next.__next__:
            v2, v3 = (v2.__next__, v3.next.__next__)
        v2.next = v2.next.__next__
        return v1.__next__

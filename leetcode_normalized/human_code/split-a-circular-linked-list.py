class C1(object):

    def __init__(self, a1=0, a2=None):
        pass

class C2(object):

    def splitCircularLinkedList(self, a1):
        """
        """
        v1 = a1
        v2, v3 = (v1, v1.__next__)
        while v1 != v3.__next__:
            v2 = v2.__next__
            v3 = v3.next.__next__ if v1 != v3.next.__next__ else v3.__next__
        v4 = v2.__next__
        v2.next, v3.next = (v1, v4)
        return [v1, v4]

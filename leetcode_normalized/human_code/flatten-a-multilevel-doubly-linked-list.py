class C1(object):

    def __init__(self, a1, a2, a3, a4):
        self.val = a1
        self.prev = a2
        self.next = a3
        self.child = a4

class C2(object):

    def flatten(self, a1):
        """
        """
        v1 = a1
        while v1:
            if v1.child:
                v2 = v1.__next__
                v1.child.prev = v1
                v1.next = v1.child
                v3 = v1
                while v3.__next__:
                    v3 = v3.__next__
                if v2:
                    v3.next = v2
                    v2.prev = v3
                v1.child = None
            v1 = v1.__next__
        return a1

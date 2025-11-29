class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return 'Nil'
        else:
            return '{} -> {}'.format(self.val, repr(self.__next__))

class C2(object):

    def connect(self, a1):
        v1 = a1
        while v1:
            v2 = v1
            while v2 and v2.left:
                v2.left.next = v2.right
                if v2.__next__:
                    v2.right.next = v2.next.left
                v2 = v2.__next__
            v1 = v1.left

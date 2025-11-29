class C1(object):

    def connect(self, a1):
        if a1 is None:
            return
        if a1.left:
            a1.left.next = a1.right
        if a1.right and a1.__next__:
            a1.right.next = a1.next.left
        self.connect(a1.left)
        self.connect(a1.right)

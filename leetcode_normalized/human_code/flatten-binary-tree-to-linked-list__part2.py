class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):
    v1 = None

    def flatten(self, a1):
        if a1:
            self.flatten(a1.right)
            self.flatten(a1.left)
            a1.right = self.list_head
            a1.left = None
            self.list_head = a1

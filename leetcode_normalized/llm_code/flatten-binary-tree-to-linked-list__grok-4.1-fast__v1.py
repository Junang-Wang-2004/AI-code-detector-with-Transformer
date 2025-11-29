class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def flatten(self, a1):
        v1 = a1
        while v1:
            if v1.left:
                v2 = v1.left
                while v2.right:
                    v2 = v2.right
                v2.right = v1.right
                v1.right = v1.left
                v1.left = None
            v1 = v1.right

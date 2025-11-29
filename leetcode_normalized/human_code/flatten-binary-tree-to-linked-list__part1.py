class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def flatten(self, a1):
        self.flattenRecu(a1, None)

    def flattenRecu(self, a1, a2):
        if a1:
            a2 = self.flattenRecu(a1.right, a2)
            a2 = self.flattenRecu(a1.left, a2)
            a1.right = a2
            a1.left = None
            return a1
        else:
            return a2

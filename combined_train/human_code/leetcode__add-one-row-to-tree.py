class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def addOneRow(self, a1, a2, a3):
        """
        """
        if a3 in (0, 1):
            v1 = C1(a2)
            if a3 == 1:
                v1.left = a1
            else:
                v1.right = a1
            return v1
        if a1 and a3 >= 2:
            a1.left = self.addOneRow(a1.left, a2, a3 - 1 if a3 > 2 else 1)
            a1.right = self.addOneRow(a1.right, a2, a3 - 1 if a3 > 2 else 0)
        return a1

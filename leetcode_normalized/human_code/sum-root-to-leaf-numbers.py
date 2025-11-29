class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def sumNumbers(self, a1):
        return self.sumNumbersRecu(a1, 0)

    def sumNumbersRecu(self, a1, a2):
        if a1 is None:
            return 0
        if a1.left is None and a1.right is None:
            return a2 * 10 + a1.val
        return self.sumNumbersRecu(a1.left, a2 * 10 + a1.val) + self.sumNumbersRecu(a1.right, a2 * 10 + a1.val)

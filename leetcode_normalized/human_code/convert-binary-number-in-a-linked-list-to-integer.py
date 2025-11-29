class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def getDecimalValue(self, a1):
        """
        """
        v1 = 0
        while a1:
            v1 = v1 * 2 + a1.val
            a1 = a1.__next__
        return v1

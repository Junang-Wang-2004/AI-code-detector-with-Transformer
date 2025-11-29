class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def getDecimalValue(self, a1):
        if not a1:
            return 0
        return self.getDecimalValue(a1.next) << 1 | a1.val

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def addTwoNumbers(self, a1, a2):
        """
        """
        v1 = C1(0)
        v2, v3 = (v1, 0)
        while a1 or a2:
            v4 = v3
            if a1:
                v4 += a1.val
                a1 = a1.__next__
            if a2:
                v4 += a2.val
                a2 = a2.__next__
            v3, v4 = divmod(v4, 10)
            v2.next = C1(v4)
            v2 = v2.__next__
        if v3 == 1:
            v2.next = C1(1)
        return v1.__next__

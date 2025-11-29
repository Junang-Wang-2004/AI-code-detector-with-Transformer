class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def plusOne(self, a1):
        """
        """
        if not a1:
            return None
        v1 = C1(0)
        v1.next = a1
        v2, v3 = (v1, a1)
        while v3.__next__:
            if v3.val != 9:
                v2 = v3
            v3 = v3.__next__
        if v3.val != 9:
            v3.val += 1
        else:
            v2.val += 1
            v3 = v2.__next__
            while v3:
                v3.val = 0
                v3 = v3.__next__
        return v1 if v1.val else v1.__next__

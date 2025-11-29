class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def deleteDuplicates(self, a1):
        """
        """
        v1 = a1
        while v1:
            v2 = v1.__next__
            while v2 and v2.val == v1.val:
                v2 = v2.__next__
            v1.next = v2
            v1 = v2
        return a1

    def deleteDuplicates2(self, a1):
        """
        """
        if not a1:
            return a1
        if a1.__next__:
            if a1.val == a1.next.val:
                a1 = self.deleteDuplicates2(a1.__next__)
            else:
                a1.next = self.deleteDuplicates2(a1.next)
        return a1

class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def mergeTwoLists(self, a1, a2):
        if not a1:
            return a2
        if not a2:
            return a1
        if a1.val < a2.val:
            a1.next = self.mergeTwoLists(a1.next, a2)
            return a1
        a2.next = self.mergeTwoLists(a1, a2.next)
        return a2

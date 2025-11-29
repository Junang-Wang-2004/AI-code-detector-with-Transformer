class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def sortLinkedList(self, a1):
        """
        """
        v1, v2, a1.next = (a1, a1.next, None)
        while v2:
            if v2.val > 0:
                v2.next, v1.next, v1, v2 = (None, v2, v2, v2.next)
            else:
                v2.next, a1, v2 = (a1, v2, v2.next)
        return a1

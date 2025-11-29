class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def sortLinkedList(self, a1):
        v1 = C1()
        v2 = C1()
        v3 = v1
        v4 = v2
        v5 = a1
        while v5:
            if v5.val > 0:
                v4.next = v5
                v4 = v5
            else:
                v3.next = v5
                v3 = v5
            v5 = v5.next
        v3.next = v2.next
        return v1.next

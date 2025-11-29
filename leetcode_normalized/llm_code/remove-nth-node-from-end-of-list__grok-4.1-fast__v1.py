class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def removeNthFromEnd(self, a1, a2):
        v1 = C1(0)
        v1.next = a1
        v2 = v1
        for v3 in range(a2 + 1):
            v2 = v2.next
        v4 = v1
        while v2:
            v4 = v4.next
            v2 = v2.next
        v4.next = v4.next.next
        return v1.next

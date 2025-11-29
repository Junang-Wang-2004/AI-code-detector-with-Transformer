class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def swapPairs(self, a1):
        if a1 is None or a1.next is None:
            return a1
        v1 = a1.next
        a1.next = v1.next
        v1.next = a1
        v2 = a1
        v3 = v2.next
        while v3 is not None and v3.next is not None:
            v2.next = v3.next
            v3.next = v2.next.next
            v2.next.next = v3
            v2 = v3
            v3 = v2.next
        return v1

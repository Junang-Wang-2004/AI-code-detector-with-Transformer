class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def reverseList(self, a1):
        v1 = None
        v2 = a1
        while v2:
            v3 = v2.next
            v2.next = v1
            v1 = v2
            v2 = v3
        return v1

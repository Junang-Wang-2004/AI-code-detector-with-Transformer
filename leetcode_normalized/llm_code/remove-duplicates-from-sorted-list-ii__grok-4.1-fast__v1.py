class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def deleteDuplicates(self, a1):
        v1 = C1(-1)
        v1.next = a1
        v2 = v1
        while v2.next:
            if v2.next.next and v2.next.val == v2.next.next.val:
                v3 = v2.next.val
                while v2.next and v2.next.val == v3:
                    v2.next = v2.next.next
            else:
                v2 = v2.next
        return v1.next

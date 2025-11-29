class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def deleteDuplicates(self, a1):
        v1 = None
        v2 = a1
        while v2:
            if v1 and v1.val == v2.val:
                v1.next = v2.next
            else:
                v1 = v2
            v2 = v2.next
        return a1

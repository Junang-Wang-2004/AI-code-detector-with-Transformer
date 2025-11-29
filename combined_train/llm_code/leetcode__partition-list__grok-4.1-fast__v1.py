class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def partition(self, a1, a2):
        v1 = C1(0)
        v2 = C1(0)
        v3 = v1
        v4 = v2
        v5 = a1
        while v5:
            if v5.val < a2:
                v3.next = v5
                v3 = v3.next
            else:
                v4.next = v5
                v4 = v4.next
            v5 = v5.next
        v3.next = v2.next
        v4.next = None
        return v1.next

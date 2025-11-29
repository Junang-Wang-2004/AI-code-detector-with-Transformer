class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def sortList(self, a1: C1) -> C1:
        if not a1 or not a1.next:
            return a1
        v1, v2 = (a1, a1.next)
        while v2 and v2.next:
            v1 = v1.next
            v2 = v2.next.next
        v3 = v1.next
        v1.next = None
        v4 = self.sortList(a1)
        v5 = self.sortList(v3)
        return self._merge(v4, v5)

    def _merge(self, a1: C1, a2: C1) -> C1:
        v1 = C1()
        v2 = v1
        while a1 and a2:
            if a1.val <= a2.val:
                v2.next = a1
                a1 = a1.next
            else:
                v2.next = a2
                a2 = a2.next
            v2 = v2.next
        v2.next = a1 or a2
        return v1.next

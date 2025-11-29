class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def detectCycle(self, a1):
        if not a1:
            return None
        v1 = a1
        v2 = a1
        while v2:
            if not v2.next:
                return None
            v2 = v2.next.next
            v1 = v1.next
            if v1 == v2:
                break
            if not v1:
                return None
        else:
            return None
        v2 = a1
        while v2 != v1:
            v2 = v2.next
            v1 = v1.next
        return v2

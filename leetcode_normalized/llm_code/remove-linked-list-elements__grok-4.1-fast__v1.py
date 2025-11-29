class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def removeElements(self, a1, a2):
        while a1 and a1.val == a2:
            a1 = a1.next
        if not a1:
            return None
        v2 = a1
        v3 = a1.next
        while v3:
            if v3.val == a2:
                v2.next = v3.next
            else:
                v2 = v3
            v3 = v3.next
        return a1

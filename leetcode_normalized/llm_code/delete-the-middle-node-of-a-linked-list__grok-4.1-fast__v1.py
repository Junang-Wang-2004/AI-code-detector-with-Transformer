class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def deleteMiddle(self, a1):
        if not a1:
            return None
        v1 = 0
        v2 = a1
        while v2:
            v1 += 1
            v2 = v2.next
        v3 = v1 // 2
        if v3 == 0:
            return a1.next
        v4 = a1
        for v5 in range(v3 - 1):
            v4 = v4.next
        v4.next = v4.next.next
        return a1

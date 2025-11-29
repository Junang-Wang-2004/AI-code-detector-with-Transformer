class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def rotateRight(self, a1, a2):
        if not a1 or a1.next is None:
            return a1
        v1 = 1
        v2 = a1
        while v2.next:
            v2 = v2.next
            v1 += 1
        v3 = v2
        a2 %= v1
        if a2 == 0:
            return a1
        v5 = a1
        for v6 in range(v1 - a2 - 1):
            v5 = v5.next
        v7 = v5.next
        v5.next = None
        v3.next = a1
        return v7

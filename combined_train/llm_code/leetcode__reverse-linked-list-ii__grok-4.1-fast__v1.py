class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def reverseBetween(self, a1, a2, a3):
        v1 = C1(0)
        v1.next = a1
        v2 = v1
        for v3 in range(a2 - 1):
            v2 = v2.next
        v4 = v2.next
        v5 = a3 - a2 + 1
        v6 = v2
        v7 = v2.next
        while v5 > 0:
            v8 = v7.next
            v7.next = v6
            v6 = v7
            v7 = v8
            v5 -= 1
        v2.next = v6
        v4.next = v7
        return v1.next

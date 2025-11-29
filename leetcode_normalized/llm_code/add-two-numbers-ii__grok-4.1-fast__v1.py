class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def addTwoNumbers(self, a1, a2):
        v1 = C1(0)
        v2 = v1
        v3 = 0
        while a1 or a2 or v3:
            v4 = a1.val if a1 else 0
            v5 = a2.val if a2 else 0
            v6 = v4 + v5 + v3
            v3 = v6 // 10
            v2.next = C1(v6 % 10)
            v2 = v2.next
            a1 = a1.next if a1 else None
            a2 = a2.next if a2 else None
        return v1.next

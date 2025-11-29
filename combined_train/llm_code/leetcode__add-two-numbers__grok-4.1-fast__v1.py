class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def addTwoNumbers(self, a1, a2):
        v1 = None
        v2 = None
        v3 = 0
        while a1 or a2 or v3:
            v4 = a1.val if a1 else 0
            v5 = a2.val if a2 else 0
            v6 = v4 + v5 + v3
            v7 = C1(v6 % 10)
            if v2 is None:
                v2 = v7
            else:
                v1.next = v7
            v1 = v7
            v3 = v6 // 10
            if a1:
                a1 = a1.next
            if a2:
                a2 = a2.next
        return v2

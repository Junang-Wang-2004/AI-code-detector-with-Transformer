class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def reorderList(self, a1):
        if not a1 or not a1.next:
            return a1
        v1 = a1
        v2 = a1.next
        while v2 and v2.next:
            v1 = v1.next
            v2 = v2.next.next
        v3 = v1.next
        v1.next = None
        v4 = None
        v5 = v3
        while v5:
            v6 = v5.next
            v5.next = v4
            v4 = v5
            v5 = v6
        v7 = a1
        v8 = v4
        while v7 and v8:
            v9 = v7.next
            v10 = v8.next
            v7.next = v8
            v8.next = v9
            v7 = v9
            v8 = v10
        return a1

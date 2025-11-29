class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def pairSum(self, a1):
        v1 = v2 = a1
        while v2.next and v2.next.next:
            v1 = v1.next
            v2 = v2.next.next
        v3 = None
        v4 = v1.next
        while v4:
            v5 = v4.next
            v4.next = v3
            v3 = v4
            v4 = v5
        v6 = 0
        v7 = a1
        v8 = v3
        while v7 and v8:
            v6 = max(v6, v7.val + v8.val)
            v7 = v7.next
            v8 = v8.next
        return v6

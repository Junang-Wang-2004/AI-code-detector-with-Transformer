class C1:

    def oddEvenList(self, a1):
        if not a1 or not a1.next:
            return a1
        v1 = a1
        v2 = a1.next
        v3 = v2
        while v3 and v3.next:
            v4 = v3.next
            v1.next = v4
            v1 = v4
            v3.next = v4.next
            v3 = v3.next
        v1.next = v2
        return a1

class C1:

    def insertionSortList(self, a1):
        v1 = ListNode(0)
        v1.next = None
        v2 = a1
        while v2:
            v3 = v2.next
            v4 = v1
            while v4.next and v4.next.val <= v2.val:
                v4 = v4.next
            v2.next = v4.next
            v4.next = v2
            v2 = v3
        return v1.next

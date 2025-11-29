class C1:

    def frequenciesOfElements(self, a1):
        v1 = ListNode(0)
        v2 = v1
        while a1:
            v3 = 1
            v4 = a1.next
            while v4 and v4.val == a1.val:
                v3 += 1
                v4 = v4.next
            v2.next = ListNode(v3)
            v2 = v2.next
            a1 = v4
        return v1.next

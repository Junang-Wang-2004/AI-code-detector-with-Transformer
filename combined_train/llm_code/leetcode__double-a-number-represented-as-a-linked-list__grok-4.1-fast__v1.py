class C1:

    def doubleIt(self, a1):

        def reverse(a1):
            v1 = None
            v2 = a1
            while v2:
                v3 = v2.next
                v2.next = v1
                v1 = v2
                v2 = v3
            return v1
        v1 = reverse(a1)
        v2 = 0
        v3 = None
        v4 = v1
        while v4:
            v5 = v4.val * 2 + v2
            v4.val = v5 % 10
            v2 = v5 // 10
            v3 = v4
            v4 = v4.next
        if v2:
            v3.next = ListNode(v2)
        return reverse(v1)

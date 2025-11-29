class C1:

    def isPalindrome(self, a1):
        if not a1 or not a1.next:
            return True
        v1 = a1
        v2 = a1
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
        v6 = a1
        v7 = v3
        while v7:
            if v6.val != v7.val:
                return False
            v6 = v6.next
            v7 = v7.next
        return True

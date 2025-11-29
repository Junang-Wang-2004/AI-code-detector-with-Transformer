class C1(object):

    def modifiedList(self, a1, a2):
        """
        """
        v1 = set(a1)
        v2 = v3 = ListNode(0, a2)
        while v2.__next__:
            if v2.next.val not in v1:
                v2 = v2.__next__
            else:
                v2.next = v2.next.__next__
        return v3.__next__

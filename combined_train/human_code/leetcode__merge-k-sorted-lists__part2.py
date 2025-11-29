class C1(object):

    def mergeKLists(self, a1):

        def mergeTwoLists(a1, a2):
            v1 = v2 = ListNode(0)
            while a1 and a2:
                if a1.val < a2.val:
                    v1.next = a1
                    a1 = a1.__next__
                else:
                    v1.next = a2
                    a2 = a2.__next__
                v1 = v1.__next__
            v1.next = a1 or a2
            return v2.__next__

        def mergeKListsHelper(a1, a2, a3):
            if a2 > a3:
                return None
            if a2 == a3:
                return a1[a2]
            return mergeTwoLists(mergeKListsHelper(a1, a2, (a2 + a3) / 2), mergeKListsHelper(a1, (a2 + a3) / 2 + 1, a3))
        return mergeKListsHelper(a1, 0, len(a1) - 1)

class C1:

    def modifiedList(self, a1, a2):
        v1 = set(a1)
        v2 = None
        v3 = a2
        while v3:
            if v3.val in v1:
                if v2 is None:
                    a2 = v3.next
                else:
                    v2.next = v3.next
            else:
                v2 = v3
            v3 = v3.next
        return a2

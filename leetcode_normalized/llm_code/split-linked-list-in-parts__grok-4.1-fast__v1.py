class C1:

    def splitListToParts(self, a1, a2):
        v1 = 0
        v2 = a1
        while v2 is not None:
            v1 += 1
            v2 = v2.next
        v3 = v1 // a2
        v4 = v1 % a2
        v5 = []
        v2 = a1
        for v6 in range(a2):
            v5.append(v2)
            v7 = v3 + (1 if v6 < v4 else 0) - 1
            for v8 in range(v7):
                if v2 is None:
                    break
                v2 = v2.next
            if v2 is not None:
                v9 = v2.next
                v2.next = None
                v2 = v9
        return v5

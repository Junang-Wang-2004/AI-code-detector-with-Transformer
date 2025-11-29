class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def reverseEvenLengthGroups(self, a1):
        v1 = a1
        v2 = 2
        while v1 and v1.next:
            v3 = v1
            v4 = 0
            for v5 in range(v2):
                if not v3.next:
                    break
                v4 += 1
                v3 = v3.next
            v2 += 1
            if v4 % 2 != 0:
                v1 = v3
                continue
            v6 = v1.next
            v7 = None
            v8 = v6
            for v5 in range(v4):
                v9 = v8.next
                v8.next = v7
                v7 = v8
                v8 = v9
            v6.next = v8
            v1.next = v7
            v1 = v6
        return a1

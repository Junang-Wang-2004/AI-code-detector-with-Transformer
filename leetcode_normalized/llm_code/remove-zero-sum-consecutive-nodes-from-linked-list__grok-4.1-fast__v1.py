class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def removeZeroSumSublists(self, a1):
        v1 = C1(0, a1)
        v2 = {0: v1}
        v3 = v1
        v4 = 0
        while v3:
            v4 += v3.val
            if v4 in v2:
                v2[v4].next = v3.next
            else:
                v2[v4] = v3
            v3 = v3.next
        return v1.next

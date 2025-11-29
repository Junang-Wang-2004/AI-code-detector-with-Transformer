class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def mergeNodes(self, a1):
        v1 = a1
        while v1.next:
            v2 = 0
            v3 = v1.next
            while v3.val != 0:
                v2 += v3.val
                v3 = v3.next
            v1.val += v2
            if not v3.next:
                v1.next = None
                break
            v1.next = v3
            v1 = v3
        return a1

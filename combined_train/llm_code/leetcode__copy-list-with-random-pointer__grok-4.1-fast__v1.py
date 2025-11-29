class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None
        self.random = None

class C2:

    def copyRandomList(self, a1):
        if not a1:
            return None
        v1 = {}
        v2 = a1
        while v2:
            v1[v2] = C1(v2.val)
            v2 = v2.next
        v3 = v1[a1]
        v2 = a1
        while v2:
            v4 = v1[v2]
            v4.next = v1.get(v2.next, None)
            v4.random = v1.get(v2.random, None)
            v2 = v2.next
        return v3

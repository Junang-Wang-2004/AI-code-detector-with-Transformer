class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def getIntersectionNode(self, a1, a2):

        def length(a1):
            v1 = 0
            v2 = a1
            while v2:
                v1 += 1
                v2 = v2.next
            return v1
        v1 = length(a1)
        v2 = length(a2)
        v3 = a1
        v4 = a2
        if v1 > v2:
            for v5 in range(v1 - v2):
                v3 = v3.next
        elif v2 > v1:
            for v5 in range(v2 - v1):
                v4 = v4.next
        while v3 != v4:
            v3 = v3.next
            v4 = v4.next
        return v3

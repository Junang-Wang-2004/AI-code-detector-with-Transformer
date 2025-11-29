class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def deleteDuplicatesUnsorted(self, a1):
        v1 = {}
        v2 = a1
        while v2:
            v3 = v2.val
            v1[v3] = v1.get(v3, 0) + 1
            v2 = v2.next
        v4 = []
        v2 = a1
        while v2:
            if v1[v2.val] == 1:
                v4.append(v2)
            v2 = v2.next
        if not v4:
            return None
        for v5 in range(len(v4) - 1):
            v4[v5].next = v4[v5 + 1]
        v4[-1].next = None
        return v4[0]

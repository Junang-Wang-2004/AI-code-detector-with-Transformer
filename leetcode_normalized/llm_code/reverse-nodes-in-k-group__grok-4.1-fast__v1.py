class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def reverseKGroup(self, a1, a2):
        v1 = C1(0)
        v1.next = a1
        v2 = v1
        while True:
            v3 = v2
            for v4 in range(a2):
                v3 = v3.next
                if v3 is None:
                    return v1.next
            v5 = v2.next
            v6 = self._reverse_group(v5, a2)
            v2.next = v6
            v2 = v5

    def _reverse_group(self, a1, a2):
        v1 = None
        v2 = a1
        for v3 in range(a2):
            v4 = v2.next
            v2.next = v1
            v1 = v2
            v2 = v4
        a1.next = v2
        return v1

class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def hasCycle(self, a1):
        v1 = set()
        v2 = a1
        while v2 is not None:
            if v2 in v1:
                return True
            v1.add(v2)
            v2 = v2.next
        return False

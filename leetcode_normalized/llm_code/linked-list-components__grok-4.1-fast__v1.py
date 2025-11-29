class C1:

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2:

    def numComponents(self, a1, a2):
        v1 = set(a2)
        v2 = 0
        v3 = a1
        v4 = False
        while v3:
            v5 = v3.val in v1
            if v5 and (not v4):
                v2 += 1
            v4 = v5
            v3 = v3.next
        return v2

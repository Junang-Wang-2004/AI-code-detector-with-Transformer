class C1:

    def __init__(self, a1=0, a2=0, a3=None):
        self.coefficient = a1
        self.power = a2
        self.next = a3

class C2:

    def addPoly(self, a1, a2):
        v1 = C1()
        v2 = v1
        while a1 or a2:
            if not a1:
                v2.next = a2
                a2 = a2.next
            elif not a2:
                v2.next = a1
                a1 = a1.next
            elif a1.power > a2.power:
                v2.next = a1
                a1 = a1.next
            elif a1.power < a2.power:
                v2.next = a2
                a2 = a2.next
            else:
                v5 = a1.coefficient + a2.coefficient
                a1 = a1.next
                a2 = a2.next
                if v5 != 0:
                    v2.next = C1(v5, a1.power if a1 else a2.power)
            if v2.next:
                v2 = v2.next
        return v1.next

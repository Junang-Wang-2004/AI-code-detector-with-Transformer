class C1:

    def __init__(self, a1=0, a2=0, a3=None):
        pass

class C2:

    def addPoly(self, a1, a2):
        """
        """
        v1 = v2 = C1()
        while a1 and a2:
            if a1.power > a2.power:
                v1.next = a1
                v1 = v1.__next__
                a1 = a1.__next__
            elif a1.power < a2.power:
                v1.next = a2
                v1 = v1.__next__
                a2 = a2.__next__
            else:
                v5 = a1.coefficient + a2.coefficient
                if v5:
                    v1.next = C1(v5, a1.power)
                    v1 = v1.__next__
                a1, a2 = (a1.__next__, a2.__next__)
        v1.next = a1 or a2
        return v2.__next__

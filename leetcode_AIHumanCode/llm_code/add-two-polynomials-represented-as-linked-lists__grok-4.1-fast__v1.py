class PolyNode:
    def __init__(self, coefficient=0, power=0, next=None):
        self.coefficient = coefficient
        self.power = power
        self.next = next


class Solution:
    def addPoly(self, pa, pb):
        head = PolyNode()
        walker = head
        while pa or pb:
            if not pa:
                walker.next = pb
                pb = pb.next
            elif not pb:
                walker.next = pa
                pa = pa.next
            elif pa.power > pb.power:
                walker.next = pa
                pa = pa.next
            elif pa.power < pb.power:
                walker.next = pb
                pb = pb.next
            else:
                combined = pa.coefficient + pb.coefficient
                pa = pa.next
                pb = pb.next
                if combined != 0:
                    walker.next = PolyNode(combined, pa.power if pa else pb.power)
            if walker.next:
                walker = walker.next
        return head.next

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def addTwoNumbers(self, a1, a2):
        """
        """
        v1, v2 = ([], [])
        while a1:
            v1.append(a1.val)
            a1 = a1.__next__
        while a2:
            v2.append(a2.val)
            a2 = a2.__next__
        v5, v6 = (None, None)
        sum = 0
        while v1 or v2:
            sum /= 10
            if v1:
                sum += v1.pop()
            if v2:
                sum += v2.pop()
            v6 = C1(sum % 10)
            v6.next = v5
            v5 = v6
        if sum >= 10:
            v6 = C1(sum / 10)
            v6.next = v5
        return v6

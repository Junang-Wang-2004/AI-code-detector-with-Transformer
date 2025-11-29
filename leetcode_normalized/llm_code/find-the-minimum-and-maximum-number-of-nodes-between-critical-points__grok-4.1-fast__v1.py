class C1:

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2:

    def nodesBetweenCriticalPoints(self, a1):
        v1 = []
        v2 = 1
        v3 = a1
        while v3.next and v3.next.next:
            if v3.next.val > v3.val and v3.next.val > v3.next.next.val or (v3.next.val < v3.val and v3.next.val < v3.next.next.val):
                v1.append(v2 + 1)
            v2 += 1
            v3 = v3.next
        if len(v1) < 2:
            return [-1, -1]
        v4 = min((v1[j + 1] - v1[j] for v5 in range(len(v1) - 1)))
        return [v4, v1[-1] - v1[0]]

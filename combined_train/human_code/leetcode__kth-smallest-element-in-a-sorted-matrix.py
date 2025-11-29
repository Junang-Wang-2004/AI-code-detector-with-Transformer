from heapq import heappush, heappop

class C1(object):

    def kthSmallest(self, a1, a2):
        """
        """
        v1 = 0
        v2 = []

        def push(a1, a2):
            if len(a1) > len(a1[0]):
                if a1 < len(a1[0]) and a2 < len(a1):
                    heappush(v2, [a1[a2][a1], a1, a2])
            elif a1 < len(a1) and a2 < len(a1[0]):
                heappush(v2, [a1[a1][a2], a1, a2])
        push(0, 0)
        while v2 and a2 > 0:
            v1, v3, v4 = heappop(v2)
            push(v3, v4 + 1)
            if v4 == 0:
                push(v3 + 1, 0)
            a2 -= 1
        return v1

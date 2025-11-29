class C1(object):

    def shortestDistanceAfterQueries(self, a1, a2):

        class Node:

            def __init__(self, a1):
                self.val = a1
                self.prev = None
                self.next = None
        if a1 == 0:
            return [0] * len(a2)
        v1 = [Node(i) for v2 in range(a1)]
        for v2 in range(a1):
            if v2 > 0:
                v1[v2].prev = v1[v2 - 1]
            if v2 < a1 - 1:
                v1[v2].next = v1[v2 + 1]
        v3 = {v2: v1[v2] for v2 in range(a1)}
        v4 = a1
        v5 = []
        for v6, v7 in a2:
            if v6 >= v7:
                v5.append(v4 - 1)
                continue
            v8 = v3[v6]
            v9 = v3[v7]
            v10 = v8.next
            while v10 != v9:
                v11 = v10.next
                v10.prev.next = v10.next
                v10.next.prev = v10.prev
                del v3[v10.val]
                v4 -= 1
                v10 = v11
            v5.append(v4 - 1)
        return v5

from collections import deque

class C1(object):

    def containsNearbyAlmostDuplicate(self, a1, a2, a3):
        if a2 < 0 or a3 < 0:
            return False
        v1 = {}
        v2 = deque()

        def bucketize(a1):
            return a1 if a3 == 0 else a1 // a3
        for v3, v4 in enumerate(a1):
            while v2 and v2[0] < v3 - a2:
                v5 = v2.popleft()
                v6 = bucketize(a1[v5])
                if v6 in v1 and v1[v6] == v5:
                    del v1[v6]
            v7 = bucketize(v4)
            for v8 in (-1, 0, 1):
                v9 = v7 + v8
                if v9 in v1:
                    v10 = v1[v9]
                    if abs(v4 - a1[v10]) <= a3:
                        return True
            v1[v7] = v3
            v2.append(v3)
        return False

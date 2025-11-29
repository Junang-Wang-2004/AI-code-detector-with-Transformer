from collections import deque

class C1(object):

    def countSteppingNumbers(self, a1, a2):
        v1 = []
        v2 = set()
        v3 = deque()
        for v4 in range(10):
            if v4 <= a2:
                v3.append(v4)
                v2.add(v4)
        while v3:
            v5 = v3.popleft()
            if v5 >= a1:
                v1.append(v5)
            v6 = v5 % 10
            for v7 in (-1, 1):
                v8 = v6 + v7
                if 0 <= v8 <= 9:
                    v9 = v5 * 10 + v8
                    if v9 <= a2 and v9 not in v2:
                        v2.add(v9)
                        v3.append(v9)
        return v1

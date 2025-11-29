from collections import deque

class C1(object):

    def minKBitFlips(self, a1, a2):
        v1 = len(a1)
        v2 = deque()
        v3 = 0
        v4 = 0
        for v5 in range(v1):
            if v2 and v2[0] == v5 - a2:
                v2.popleft()
                v3 ^= 1
            if a1[v5] == v3:
                if v5 + a2 > v1:
                    return -1
                v2.append(v5)
                v3 ^= 1
                v4 += 1
        return v4

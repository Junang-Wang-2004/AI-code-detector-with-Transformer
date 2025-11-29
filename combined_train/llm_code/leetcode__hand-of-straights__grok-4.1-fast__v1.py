from collections import Counter

class C1(object):

    def isNStraightHand(self, a1, a2):
        if len(a1) % a2 != 0:
            return False
        v1 = Counter(a1)
        v2 = sorted(v1)
        v3 = len(a1) // a2
        for v4 in range(v3):
            v5 = 0
            while v5 < len(v2) and v1[v2[v5]] == 0:
                v5 += 1
            if v5 == len(v2):
                return False
            v6 = v2[v5]
            v7 = v6
            for v4 in range(a2):
                if v1[v7] == 0:
                    return False
                v1[v7] -= 1
                v7 += 1
        return True

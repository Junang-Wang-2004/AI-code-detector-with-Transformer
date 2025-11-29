from collections import Counter

class C1:

    def isPossible(self, a1):
        v1 = Counter(a1)
        v2 = Counter()
        for v3 in a1:
            if v1[v3] == 0:
                continue
            v1[v3] -= 1
            if v2[v3 - 1] > 0:
                v2[v3 - 1] -= 1
                v2[v3] += 1
            elif v1[v3 + 1] > 0 and v1[v3 + 2] > 0:
                v1[v3 + 1] -= 1
                v1[v3 + 2] -= 1
                v2[v3 + 2] += 1
            else:
                return False
        return True

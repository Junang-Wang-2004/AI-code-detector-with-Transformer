from collections import defaultdict

class C1(object):

    def firstUniqChar(self, a1):
        """
        """
        v1 = defaultdict(int)
        v2 = set()
        for v3, v4 in enumerate(a1):
            if v1[v4]:
                v2.discard(v1[v4])
            else:
                v1[v4] = v3 + 1
                v2.add(v3 + 1)
        return min(v2) - 1 if v2 else -1

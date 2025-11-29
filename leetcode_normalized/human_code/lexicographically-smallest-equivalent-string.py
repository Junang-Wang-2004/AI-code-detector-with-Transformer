class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        self.set[max(v1, v2)] = min(v1, v2)
        return True

class C2(object):

    def smallestEquivalentString(self, a1, a2, a3):
        """
        """
        v1 = C1(26)
        for v2 in range(len(a1)):
            v1.union_set(ord(a1[v2]) - ord('a'), ord(a2[v2]) - ord('a'))
        v3 = []
        for v2 in range(len(a3)):
            v4 = v1.find_set(ord(a3[v2]) - ord('a'))
            v3.append(chr(v4 + ord('a')))
        return ''.join(v3)

class C1(object):

    def __init__(self):
        self.word_idx = -1
        self.leaves = {}

    def insert(self, a1, a2):
        v1 = self
        for v2 in a1:
            if not v2 in v1.leaves:
                v1.leaves[v2] = C1()
            v1 = v1.leaves[v2]
        v1.word_idx = a2

    def find(self, a1, a2, a3):
        v1 = self
        for v2 in reversed(range(len(a1))):
            if a1[v2] in v1.leaves:
                v1 = v1.leaves[a1[v2]]
                if v1.word_idx not in (-1, a2) and self.is_palindrome(a1, v2 - 1):
                    a3.append([v1.word_idx, a2])
            else:
                break

    def is_palindrome(self, a1, a2):
        v1 = 0
        while v1 <= a2:
            if a1[v1] != a1[a2]:
                return False
            v1 += 1
            a2 -= 1
        return True

class C2(object):

    def palindromePairs(self, a1):
        """
        """
        v1 = []
        v2 = C1()
        for v3 in range(len(a1)):
            v2.insert(a1[v3], v3)
        for v3 in range(len(a1)):
            v2.find(a1[v3], v3, v1)
        return v1

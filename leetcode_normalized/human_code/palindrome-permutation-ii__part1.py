import collections
import itertools

class C1(object):

    def generatePalindromes(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = ''.join((k for v3, v4 in v1.items() if v4 % 2))
        v5 = ''.join((v3 * (v4 / 2) for v3, v4 in v1.items()))
        return self.permuteUnique(v2, v5) if len(v2) < 2 else []

    def permuteUnique(self, a1, a2):
        v1 = []
        v2 = [False] * len(a2)
        self.permuteUniqueRecu(a1, v1, v2, [], a2)
        return v1

    def permuteUniqueRecu(self, a1, a2, a3, a4, a5):
        if len(a4) == len(a5):
            v1 = ''.join(a4)
            a2.append(v1 + a1 + v1[::-1])
            return
        for v2 in range(len(a5)):
            if not a3[v2] and (not (v2 > 0 and a5[v2 - 1] == a5[v2] and a3[v2 - 1])):
                a3[v2] = True
                a4.append(a5[v2])
                self.permuteUniqueRecu(a1, a2, a3, a4, a5)
                a4.pop()
                a3[v2] = False

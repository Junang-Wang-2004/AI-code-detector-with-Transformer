class Solution:
    def isItPossible(self, word1, word2):
        f1 = [0] * 26
        f2 = [0] * 26
        for c in word1:
            f1[ord(c) - ord('a')] += 1
        for c in word2:
            f2[ord(c) - ord('a')] += 1
        a = sum(1 for x in f1 if x > 0)
        b = sum(1 for x in f2 if x > 0)
        common = any(f1[i] > 0 and f2[i] > 0 for i in range(26))
        if a == b and common:
            return True
        for i in range(26):
            if f1[i] == 0:
                continue
            for j in range(26):
                if f2[j] == 0 or i == j:
                    continue
                na = a - (1 if f1[i] == 1 else 0) + (1 if f1[j] == 0 else 0)
                nb = b - (1 if f2[j] == 1 else 0) + (1 if f2[i] == 0 else 0)
                if na == nb:
                    return True
        return False

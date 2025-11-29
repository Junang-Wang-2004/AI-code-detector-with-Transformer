class Solution:
    def checkIfCanBreak(self, a, b):
        def dominates(x, y):
            cx = [0] * 26
            cy = [0] * 26
            for ch in x:
                cx[ord(ch) - ord('a')] += 1
            for ch in y:
                cy[ord(ch) - ord('a')] += 1
            px, py = 0, 0
            for i in range(26):
                px += cx[i]
                py += cy[i]
                if px < py:
                    return False
            return True
        return dominates(a, b) or dominates(b, a)

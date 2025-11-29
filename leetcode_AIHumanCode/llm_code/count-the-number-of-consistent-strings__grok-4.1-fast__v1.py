class Solution:
    def countConsistentStrings(self, allowed, words):
        chars = set(allowed)
        total = 0
        for w in words:
            valid = True
            for ch in w:
                if ch not in chars:
                    valid = False
                    break
            if valid:
                total += 1
        return total

class Solution:
    def isSubstringPresent(self, s):
        transitions = set()
        n = len(s)
        for i in range(n - 1):
            prev = s[i]
            curr = s[i + 1]
            if prev == curr or (curr, prev) in transitions:
                return True
            transitions.add((prev, curr))
        return False

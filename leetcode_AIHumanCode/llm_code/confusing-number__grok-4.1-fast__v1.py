class Solution:
    def confusingNumber(self, n):
        s = str(n)
        mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        allowed = set(mapping)
        if not all(c in allowed for c in s):
            return False
        rev_rot = ''.join(mapping[c] for c in reversed(s))
        return rev_rot != s

class Solution:
    def maxSubstrings(self, s):
        result = 0
        n = len(s)
        ptr = 0
        while ptr < n:
            positions = {}
            curr = ptr
            triggered = False
            while curr < n:
                ch = s[curr]
                if ch in positions:
                    if curr - positions[ch] + 1 >= 4:
                        result += 1
                        ptr = curr + 1
                        triggered = True
                        break
                else:
                    positions[ch] = curr
                curr += 1
            if not triggered:
                break
        return result

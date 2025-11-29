class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)
        idx = 0
        while idx < n and k > 0:
            curr = ord(chars[idx]) - ord('a')
            steps_to_a = min(curr, 26 - curr)
            used = min(steps_to_a, k)
            if used == steps_to_a:
                chars[idx] = 'a'
            else:
                chars[idx] = chr(ord('a') + curr - used)
            k -= used
            idx += 1
        return ''.join(chars)

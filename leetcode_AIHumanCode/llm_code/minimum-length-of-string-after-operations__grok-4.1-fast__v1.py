class Solution:
    def minimumLength(self, s: str) -> int:
        appeared = [False] * 26
        parity = [0] * 26
        a_ord = ord('a')
        for char in s:
            idx = ord(char) - a_ord
            appeared[idx] = True
            parity[idx] = 1 - parity[idx]
        total = 0
        for i in range(26):
            if appeared[i]:
                total += 2 if parity[i] == 0 else 1
        return total

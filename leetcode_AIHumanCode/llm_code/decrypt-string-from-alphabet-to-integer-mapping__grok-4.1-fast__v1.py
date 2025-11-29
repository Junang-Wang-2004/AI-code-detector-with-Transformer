class Solution:
    def freqAlphabets(self, s: str) -> str:
        pending = []
        decoded = []
        for char in s:
            if char.isdigit():
                pending.append(char)
            elif char == '#':
                last = pending.pop()
                prev = pending.pop()
                val = int(prev + last)
                decoded.append(chr(ord('a') + val - 1))
        while pending:
            val = int(pending.pop(0))
            decoded.append(chr(ord('a') + val - 1))
        return ''.join(decoded)

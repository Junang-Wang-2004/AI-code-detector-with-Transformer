class Solution:
    def getLucky(self, s, k):
        current = sum(sum(int(d) for d in str(ord(c) - ord('a') + 1)) for c in s)
        for _ in range(k - 1):
            if current < 10:
                break
            current = sum(int(d) for d in str(current))
        return current

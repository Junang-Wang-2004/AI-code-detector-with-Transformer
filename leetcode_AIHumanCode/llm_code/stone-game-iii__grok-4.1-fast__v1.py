class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        scores = [0] * (n + 1)
        for start in range(n - 1, -1, -1):
            max_gain = float('-inf')
            total = 0
            for take in range(1, min(3, n - start) + 1):
                total += stoneValue[start + take - 1]
                max_gain = max(max_gain, total - scores[start + take])
            scores[start] = max_gain
        diff = scores[0]
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"

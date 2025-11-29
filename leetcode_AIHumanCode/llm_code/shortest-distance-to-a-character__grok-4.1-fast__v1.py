class Solution:
    def shortestToChar(self, S, C):
        length = len(S)
        distances = [length] * length
        last_left = -length
        for pos in range(length):
            if S[pos] == C:
                last_left = pos
            distances[pos] = min(distances[pos], pos - last_left)
        last_right = length * 2
        for pos in range(length - 1, -1, -1):
            if S[pos] == C:
                last_right = pos
            distances[pos] = min(distances[pos], last_right - pos)
        return distances

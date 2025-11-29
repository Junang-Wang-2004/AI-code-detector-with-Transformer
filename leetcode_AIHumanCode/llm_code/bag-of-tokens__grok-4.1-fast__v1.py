class Solution:
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        max_points = 0
        current_points = 0
        while tokens:
            if P >= tokens[0]:
                P -= tokens.pop(0)
                current_points += 1
                max_points = max(max_points, current_points)
            elif current_points > 0:
                current_points -= 1
                P += tokens.pop()
            else:
                break
        return max_points

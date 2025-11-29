class Solution:
    def shortestDistance(self, words, word1, word2):
        last_a, last_b = -1, -1
        minimum = float('inf')
        for position, current in enumerate(words):
            if current == word1:
                if last_b != -1:
                    minimum = min(minimum, position - last_b)
                last_a = position
            elif current == word2:
                if last_a != -1:
                    minimum = min(minimum, position - last_a)
                last_b = position
        return minimum

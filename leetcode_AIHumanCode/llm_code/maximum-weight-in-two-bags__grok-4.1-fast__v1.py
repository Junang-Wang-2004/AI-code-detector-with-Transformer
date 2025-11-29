class Solution:
    def maxWeight(self, weights, cap1, cap2):
        states = {(0, 0)}
        for mass in weights:
            additions = set()
            for a, b in states:
                if a + mass <= cap1:
                    additions.add((a + mass, b))
                if b + mass <= cap2:
                    additions.add((a, b + mass))
            states.update(additions)
        return max(a + b for a, b in states)

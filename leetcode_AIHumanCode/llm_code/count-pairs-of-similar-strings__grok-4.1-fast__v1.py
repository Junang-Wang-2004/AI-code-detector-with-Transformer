class Solution:
    def similarPairs(self, words):
        freq = {}
        for term in words:
            key = frozenset(term)
            freq[key] = freq.get(key, 0) + 1
        pairs = 0
        for occurrences in freq.values():
            pairs += occurrences * (occurrences - 1) // 2
        return pairs

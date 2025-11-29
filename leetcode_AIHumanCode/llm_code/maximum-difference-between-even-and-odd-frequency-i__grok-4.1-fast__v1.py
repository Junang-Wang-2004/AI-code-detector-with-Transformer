class Solution:
    def maxDifference(self, s):
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        odd_freqs = []
        even_freqs = []
        for count in freq.values():
            if count % 2:
                odd_freqs.append(count)
            else:
                even_freqs.append(count)
        max_odd = max(odd_freqs) if odd_freqs else 0
        min_even = min(even_freqs) if even_freqs else float('inf')
        return max_odd - min_even

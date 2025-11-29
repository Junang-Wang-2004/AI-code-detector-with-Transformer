class Solution:
    def minimumPushes(self, word):
        counts = {}
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1
        freqs = sorted(counts.values(), reverse=True)
        total_pushes = 0
        pos = 0
        layer = 1
        num_freqs = len(freqs)
        while pos < num_freqs:
            count_per_layer = min(8, num_freqs - pos)
            for offset in range(count_per_layer):
                total_pushes += freqs[pos + offset] * layer
            pos += count_per_layer
            layer += 1
        return total_pushes

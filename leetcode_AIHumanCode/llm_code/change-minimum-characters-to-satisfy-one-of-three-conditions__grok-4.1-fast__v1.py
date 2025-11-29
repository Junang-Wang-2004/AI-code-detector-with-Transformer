class Solution(object):
    def minCharacters(self, a, b):
        freq_a = [0] * 26
        freq_b = [0] * 26
        offset = ord('a')
        for c in a:
            freq_a[ord(c) - offset] += 1
        for c in b:
            freq_b[ord(c) - offset] += 1
        max_shared = max(freq_a[i] + freq_b[i] for i in range(26))
        minimum = len(a) + len(b) - max_shared
        cum_a = [0] * 27
        cum_b = [0] * 27
        for i in range(26):
            cum_a[i + 1] = cum_a[i] + freq_a[i]
            cum_b[i + 1] = cum_b[i] + freq_b[i]
        na, nb = len(a), len(b)
        for i in range(25):
            suma = cum_a[i + 1]
            sumb = cum_b[i + 1]
            minimum = min(minimum, na - suma + sumb, nb - sumb + suma)
        return minimum

class Solution:
    def minStartingIndex(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        if n < m:
            return -1

        def z_algorithm(text):
            length = len(text)
            box = [0] * length
            start = end = 0
            for idx in range(1, length):
                if idx < end:
                    box[idx] = min(end - idx, box[idx - start])
                while idx + box[idx] < length and text[box[idx]] == text[idx + box[idx]]:
                    box[idx] += 1
                if idx + box[idx] > end:
                    start = idx
                    end = idx + box[idx]
            return box

        fwd = z_algorithm(needle + haystack)
        rev_needle = needle[::-1]
        rev_haystack = haystack[::-1]
        bwd = z_algorithm(rev_needle + rev_haystack)

        for pos in range(n - m + 1):
            prefix_len = fwd[m + pos]
            suffix_len = bwd[n - pos]
            if prefix_len + suffix_len + 1 >= m:
                return pos
        return -1

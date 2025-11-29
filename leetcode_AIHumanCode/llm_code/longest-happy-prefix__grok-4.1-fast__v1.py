class Solution:
    def longestPrefix(self, s):
        def compute_z(text):
            size = len(text)
            zvals = [0] * size
            begin, end = 0, 0
            for idx in range(1, size):
                if idx < end:
                    zvals[idx] = min(end - idx, zvals[idx - begin])
                while idx + zvals[idx] < size and text[zvals[idx]] == text[idx + zvals[idx]]:
                    zvals[idx] += 1
                if idx + zvals[idx] > end:
                    begin = idx
                    end = idx + zvals[idx]
            return zvals

        total = len(s)
        zvals = compute_z(s)
        best = 0
        for pos in range(1, total):
            if zvals[pos] >= total - pos:
                best = max(best, total - pos)
        return s[:best]

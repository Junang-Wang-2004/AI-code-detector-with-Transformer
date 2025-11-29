class Solution(object):
    def maximumLength(self, s):
        run_lengths = [[] for _ in range(26)]
        n = len(s)
        pos = 0
        while pos < n:
            ch = s[pos]
            start = pos
            while pos < n and s[pos] == ch:
                pos += 1
            run_lengths[ord(ch) - ord('a')].append(pos - start)
        max_len = 0
        for lengths in run_lengths:
            if not lengths:
                continue
            lengths.sort(reverse=True)
            max_len = max(max_len, lengths[0] - 2)
            num_runs = len(lengths)
            if num_runs >= 2:
                max_len = max(max_len, min(lengths[0] - 1, lengths[1]))
            if num_runs >= 3:
                max_len = max(max_len, lengths[2])
        return max_len if max_len > 0 else -1

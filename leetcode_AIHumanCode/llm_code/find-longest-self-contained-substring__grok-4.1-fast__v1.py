class Solution:
    def maxSubstringLength(self, text):
        n = len(text)
        starts = [n] * 26
        ends = [-1] * 26
        for i, ch in enumerate(text):
            c = ord(ch) - ord('a')
            starts[c] = min(starts[c], i)
            ends[c] = max(ends[c], i)
        ans = -1
        cand_starts = list(set(starts[k] for k in range(26) if starts[k] < n))
        for init in cand_starts:
            min_start = n + 5
            max_end = -5
            for j in range(init, n):
                c = ord(text[j]) - ord('a')
                min_start = min(min_start, starts[c])
                max_end = max(max_end, ends[c])
                if min_start >= init and max_end <= j:
                    ln = j - init + 1
                    if ln < n:
                        ans = max(ans, ln)
                if min_start < init:
                    break
        return ans

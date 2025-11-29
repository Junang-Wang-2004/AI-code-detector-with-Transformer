class Solution:
    def countBinarySubstrings(self, s):
        if not s:
            return 0
        runs = []
        cnt = 1
        last = s[0]
        for c in s[1:]:
            if c == last:
                cnt += 1
            else:
                runs.append(cnt)
                cnt = 1
                last = c
        runs.append(cnt)
        total = 0
        for i in range(1, len(runs)):
            total += min(runs[i - 1], runs[i])
        return total

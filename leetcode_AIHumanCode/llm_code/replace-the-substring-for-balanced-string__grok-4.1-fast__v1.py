class Solution:
    def balancedString(self, s):
        n = len(s)
        target = n // 4
        total = {}
        for c in s:
            total[c] = total.get(c, 0) + 1
        window = {c: 0 for c in total}
        min_len = n
        j = 0
        for i in range(n):
            window[s[i]] += 1
            while j <= i:
                valid = True
                for c in total:
                    if total[c] - window[c] > target:
                        valid = False
                        break
                if valid:
                    min_len = min(min_len, i - j + 1)
                    window[s[j]] -= 1
                    j += 1
                else:
                    break
        return min_len

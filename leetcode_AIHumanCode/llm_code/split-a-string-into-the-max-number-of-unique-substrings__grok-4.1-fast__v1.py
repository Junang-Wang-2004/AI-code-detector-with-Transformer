class Solution:
    def maxUniqueSplit(self, s):
        n = len(s)
        ans = 1
        
        def backtrack(pos, seen, count):
            nonlocal ans
            if pos == n:
                ans = max(ans, count)
                return
            if count + n - pos <= ans:
                return
            for nxt in range(pos + 1, n + 1):
                seg = s[pos:nxt]
                if seg not in seen:
                    seen.add(seg)
                    backtrack(nxt, seen, count + 1)
                    seen.remove(seg)
        
        backtrack(0, set(), 0)
        return ans

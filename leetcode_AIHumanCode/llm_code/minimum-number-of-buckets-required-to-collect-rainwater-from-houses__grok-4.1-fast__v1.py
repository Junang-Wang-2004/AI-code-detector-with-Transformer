class Solution(object):
    def minimumBuckets(self, street):
        n = len(street)
        ans = 0
        i = 0
        prev_bucket = False
        while i < n:
            if street[i] != 'H':
                prev_bucket = False
                i += 1
                continue
            if prev_bucket:
                i += 1
                prev_bucket = False
                continue
            if i + 1 < n and street[i + 1] == '.':
                ans += 1
                i += 2
                prev_bucket = True
                continue
            if i > 0 and street[i - 1] == '.':
                ans += 1
                i += 1
                prev_bucket = False
                continue
            return -1
        return ans

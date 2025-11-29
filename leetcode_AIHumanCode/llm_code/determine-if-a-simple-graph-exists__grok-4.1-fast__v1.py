class Solution(object):
    def simpleGraphExists(self, degrees):
        total = sum(degrees)
        if total % 2:
            return False
        degrees.sort(reverse=True)
        n = len(degrees)
        left = 0
        remain = total
        r = n - 1
        small = 0
        for k in range(1, n + 1):
            left += degrees[k - 1]
            remain -= degrees[k - 1]
            while r >= 0 and degrees[r] < k:
                small += degrees[r]
                r -= 1
            num = max(0, r - k + 1)
            extra = k * num + small if num > 0 else remain
            if left > k * (k - 1) + extra:
                return False
        return True

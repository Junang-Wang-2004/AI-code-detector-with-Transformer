class Solution:
    def consecutiveNumbersSum(self, n):
        m = n
        while m % 2 == 0:
            m //= 2
        cnt = 0
        i = 1
        while i * i <= m:
            if m % i == 0:
                cnt += 1
                if i != m // i:
                    cnt += 1
            i += 1
        return cnt

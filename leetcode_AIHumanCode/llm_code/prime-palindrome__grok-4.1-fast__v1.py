class Solution:
    def primePalindrome(self, N):
        small = [2, 3, 5, 7, 11]
        for p in small:
            if p >= N:
                return p

        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        digits = len(str(N))
        begin = 10 ** (digits // 2)
        for num in range(begin, 10**5 + 1):
            t = str(num)
            mirror = t[:-1][::-1]
            val = int(t + mirror)
            if val >= N and is_prime(val):
                return val

class Solution:
    def rotatedDigits(self, n: int) -> int:
        def check(num: int) -> int:
            seen_diff = False
            while num > 0:
                digit = num % 10
                if digit in (3, 4, 7):
                    return 0
                if digit in (2, 5, 6, 9):
                    seen_diff = True
                num //= 10
            return seen_diff

        count = 0
        for i in range(1, n + 1):
            count += check(i)
        return count

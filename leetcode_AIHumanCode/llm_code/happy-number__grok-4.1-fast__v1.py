class Solution:
    def isHappy(self, num: int) -> bool:
        def sum_of_squares(x: int) -> int:
            total = 0
            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total
        
        current = num
        while current != 1 and current != 4:
            current = sum_of_squares(current)
        return current == 1
